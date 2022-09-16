#! /usr/bin/env python3

##############################################################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.15 - 2022.09.16
# Topic: ROS2 Lab day 12 -- ROS2 Project / Catch Turtle
#
# ### chaseControl Node ##################################
#
# This node triggers the "trigger_turSpawn" service in the the
# "node_turSpawn" node, clears turtlesim using the turtlesim service,
# and kills the new turtle using the turtlesim service
#
# These services are called after certain conditions have been met, 
#
# It also has a PID Controller Implementation to go to the target turtle position 
#
# ##########
#
# Thanks to: *Eng. Khaled Zoheir*
# For explaining and providing a PID Controller Code example.
#
##############################################################################################


import rclpy

from rclpy.node import Node

from example_interfaces.srv import Trigger
from turtlesim.srv import Kill
from std_srvs.srv import Empty

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

import math
from math import sqrt, atan2


nodeName = "node_chaseControl"

class my_node_chaseControl(Node):

    def __init__(self):
        super().__init__(nodeName)

        ###################################################
        ############## -- New Turtle Name -- ##############
        self.newTurtleName = "Hamed_ElGaMeD" ##############
        ###################################################
        

        #################### Services #####################
        self.client_trigger_turSpawn = self.create_client(Trigger, "trigger_turSpawn")
        self.client_kill_newTur = self.create_client(Kill, "kill")
        self.client_clear = self.create_client(Empty, "clear")

        ############### Topics / Pub - Sub ###############
        self.create_subscription(Pose, self.newTurtleName+"/pose", self.subCallback_newTurPose, 10)
        self.create_subscription(Pose, "turtle1/pose", self.subCallback_tur1Pose, 10)
        self.pub_tur1Vel = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.create_timer(1/30, self.TimerPubCallback)

        self.get_logger().info("Node_Started")

    #----------------------------------------------------------------------------------------#
    ############### PID Controller Initialization ############################################
    #----------------------------------------------------------------------------------------#
        
        # Target Turtle
        self.desierd_x=0	            # Target x ### Will be later set to newTurtle Pose ###
        self.desired_y=0	            # Target y ### Will be later set to newTurtle Pose ###
        self.desired_tolerence = 0.5   # Target tolerence allowed in error_lin

        # Flags
        self.flag_reached=False         # We reached the target
        self.flag_isAlive=False         # has the new turtle spawned yet?

        # Commands
        self.lin_vel=0
        self.ang_vel=0

        ################### PIDs Gains ####################

        self.Kp_lin=1.2
        self.Ki_lin=0.000001
        self.Kd_lin=0.1

        self.Kp_ang=10
        self.Ki_ang=0
        self.Kd_ang=0.1

        ################### PIDs Errors   ####################
        self.dt=1/30                 # Consective time between to timer callbacks
        self.error_lin=0             # Linear distance to target
        self.cumm_error_lin=0
        self.error_rate_lin=0
        self.last_error_lin=0

        self.desired_theta=0        # theta current pose to target pos -> desired_theta
        self.error_ang=0            # diff desired_theta - current heading
        self.cumm_error_ang=0
        self.error_rate_ang=0
        self.last_error_ang=0

        ################### PIDs Components   ####################
        self.p_lin=0        # Proportional Term = Kp * error_lin
        self.i_lin=0        # Integration Term = Ki * cumm_error_lin
        self.d_lin=0        # Derivative Term = Kd * error_rate_lin

        self.p_ang=0
        self.i_ang=0
        self.d_ang=0

#----------------------------------------------------------------------------------------#
############### Trigger --Spawn-- Client ##########################################
#----------------------------------------------------------------------------------------#

    def service_trigger_turSpawn_client(self):
        while self.client_trigger_turSpawn.wait_for_service(timeout_sec = 0.25) == False:
            self.get_logger().warn("Waiting for [trigger_turSpawn] service")

        request = Trigger.Request()

        future_obj = self.client_trigger_turSpawn.call_async(request)
        future_obj.add_done_callback(self.future_callback_trigger_turSpawn)

    def future_callback_trigger_turSpawn(self, future_done):

        self.get_logger().info(f"Target: \"{self.newTurtleName}\" located,")
        self.get_logger().warn(f"Target Pursuit Initiated............")
        response = future_done.result()

        if response.success == True:
            self.flag_isAlive = True

#----------------------------------------------------------------------------------------#
############### --Kill-- New Turtle Client ###############################################
#----------------------------------------------------------------------------------------#   


    def service_kill_newTur_client(self):
        while self.client_kill_newTur.wait_for_service(timeout_sec = 0.25) == False:
            self.get_logger().warn("Waiting for [kill] service")

        request = Kill.Request()
        request.name = self.newTurtleName

        future_obj = self.client_kill_newTur.call_async(request)
        future_obj.add_done_callback(self.future_callback_kill_newTur)


    def future_callback_kill_newTur(self, future_done):
        
        # get_logger().error was used for coloring only
        self.get_logger().error(f"{self.newTurtleName} Was Killed in Action (KIA) ")
        self.flag_isAlive = False
        
#----------------------------------------------------------------------------------------#
############### --Clear-- Client #########################################################
#----------------------------------------------------------------------------------------#       

    def service_clear_client(self):
        while self.client_clear.wait_for_service(timeout_sec = 0.25) == False:
            self.get_logger().warn("Waiting for [clear] service")

        request = Empty.Request()
        future_obj = self.client_clear.call_async(request)


#----------------------------------------------------------------------------------------#
############### PID Controller Implementation ############################################
#----------------------------------------------------------------------------------------#

    def subCallback_newTurPose(self, msg):
        self.desierd_x = msg.x
        self.desired_y = msg.y
        


    def subCallback_tur1Pose(self, msg):

        self.now_x=msg.x
        self.now_y=msg.y
        self.now_theta=msg.theta


        ############### Calculating Errors ##############################
        # Calculating the Euclidean Distance
        self.error_lin=sqrt(((self.desierd_x-self.now_x)**2)+((self.desired_y-self.now_y)**2))
        
        # Finding the right absolute angle at which the target lies
        self.desired_theta=atan2((self.desired_y-self.now_y),(self.desierd_x-self.now_x))

        # Getting the relative angle with respect to the target, ie error angle
        self.error_ang=self.desired_theta-self.now_theta
        if self.error_ang > math.pi:
            self.error_ang -= 2*math.pi
            #print('dec')
        elif self.error_ang < -math.pi:
            self.error_ang += 2*math.pi
            #print('inc')


        ############ Linear Gain #########################################
        self.p_lin=self.error_lin*self.Kp_lin
        self.cumm_error_lin+=self.error_lin*self.dt

        self.i_lin=self.cumm_error_lin*self.Ki_lin
        self.error_rate_lin=(self.error_lin-self.last_error_lin)/self.dt

        self.d_lin=self.error_rate_lin*self.Kd_lin
        self.last_error_lin=self.error_lin

        self.lin_vel=self.p_lin + self.i_lin + self.d_lin   ## OUTPUT Linear Velocity


        ############ Angular Gain ########################################
        self.p_ang=self.error_ang*self.Kp_ang
        self.cumm_error_ang+=self.error_ang*self.dt

        self.i_ang=self.cumm_error_ang*self.Ki_ang
        self.error_rate_ang=(self.error_ang-self.last_error_ang)/self.dt

        self.d_ang=self.error_rate_ang*self.Kd_ang
        self.last_error_ang=self.error_ang

        self.ang_vel=self.p_ang + self.i_ang + self.d_ang   ## OUTPUT Angular Velocity
        

        if (abs(self.error_lin)) < self.desired_tolerence:
            self.lin_vel=0
            self.ang_vel=0
            if self.flag_reached==False:
                self.get_logger().warn(f"Target \"{self.newTurtleName}\" was acquired.")
                self.flag_reached=True
        #else:
        #    self.get_logger().warn(' lin_gain: '+str(self.lin_vel)+' ang_gain: '+str(self.ang_vel)+' error_ang: '+str(self.error_ang)+' error_lin: '+str(self.error_lin))


    def TimerPubCallback(self):
        msg = Twist()
        msg.linear.x=float(self.lin_vel)
        msg.angular.z=float(self.ang_vel)

        ###### Publishing the move message

        if self.flag_isAlive == False:
            self.service_trigger_turSpawn_client()
            self.flag_reached = False

        elif (self.flag_isAlive == True) and (self.flag_reached == False):
            self.pub_tur1Vel.publish(msg)
            
        elif (self.flag_isAlive == True) and (self.flag_reached == True) :
            self.service_kill_newTur_client()
            self.service_clear_client()
            

def main(args=None):
    rclpy.init()
    node_chaseControl = my_node_chaseControl()
    rclpy.spin(node_chaseControl)
    rclpy.shutdown()


if __name__ == "__main__":
    main()