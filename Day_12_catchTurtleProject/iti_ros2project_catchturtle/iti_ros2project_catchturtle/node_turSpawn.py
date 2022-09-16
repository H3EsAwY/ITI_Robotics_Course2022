#! /usr/bin/env python3

##############################################################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.15 - 2022.09.16
# Topic: ROS2 Lab day 12 -- ROS2 Project / Catch Turtle
#
# ### turSpawn Node ##################################
# Spawns a turtle at a random float X,Y coordinates 
# where X [1.0,10.0] , and Y [1.0,10.0]
# 
# The turtlesim spawn service is called in this node [node_turSpawn]
# when a trigger service is called in [node_chaseControl]
##############################################################################################

import rclpy
from rclpy.node import Node

from example_interfaces.srv import Trigger
from turtlesim.srv import Spawn

import random


nodeName = "node_turSpawn"



class my_turSpawn_node(Node):

    def __init__(self):
        super().__init__(nodeName)

        ############## -- New Turtle Name -- ##############
        self.newTurtleName = "Hamed_ElGaMeD" ##############
        ###################################################

        ############## Allowed X,Y spawn coordinates ################
        self.lst_xAllow = [1.0,10.0] #Allowed X spawn coordinates ###
        self.lst_yAllow = [1.0,10.0] #Allowed Y spawn coordinates ###
        #############################################################
        
        self.create_service(Trigger, "trigger_turSpawn", self.srvTrigCallback)
        self.client_turSpawn = self.create_client(Spawn, "spawn")

        
        self.get_logger().info("Node initiated")


    def srvTrigCallback(self, request, response):

        """

        """

        self.service_spawn_client()

        response.success = True
        response.message = self.newTurtleName

        return response
    
    def service_spawn_client(self):

        """
        
        """

        while self.client_turSpawn.wait_for_service(timeout_sec = 0.25) == False:
            self.get_logger().warn("Waiting for service")

        request = Spawn.Request()

        request.x = round(random.uniform(self.lst_xAllow[0],self.lst_xAllow[1]), 3)
        request.y = round(random.uniform(self.lst_yAllow[0],self.lst_yAllow[1]), 3)

        request.name = self.newTurtleName

        future_obj = self.client_turSpawn.call_async(request)

        future_obj.add_done_callback(self.future_callback)

    
        

    def future_callback(self, future_done):

        response = Spawn.Response()
        self.get_logger().info(f"{self.newTurtleName} Spawned Successfully")






def main(args=None):
    rclpy.init(args=args)
    node_turSpawn = my_turSpawn_node()
    rclpy.spin(node_turSpawn)
    rclpy.shutdown()


if __name__ == "__main__":
    main()