#! /usr/bin/env python3

######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.13
# Topic: ROS2Lab4 day 10
#
#####
# #X-Axis Boundaries:
# x=3, x=8
#
# #Y-Axis Boundaries:
# y=3, y=8
#####
# 
# 
# 
# 
######################################################



from http import client
from urllib import request
import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from std_srvs.srv import Empty

nodeName = "turtle_resetBoundary"

class my_node(Node):
    def __init__(self):
        super().__init__("turtle_resetBoundary")

        self.create_subscription(Pose, "turtle1/pose", self.subCallback,10)
        self.client = self.create_client(Empty, "reset")

        self.lst_xBounds=[3.0,8.0]
        self.lst_yBounds=[3.0,8.0]

        self.get_logger().warn("turtle_resetBoundary is running")


    def subCallback(self, msg_pose):
        
        if msg_pose.x < self.lst_xBounds[0] or \
           msg_pose.y < self.lst_yBounds[0] or \
           msg_pose.x > self.lst_xBounds[1] or \
           msg_pose.y > self.lst_yBounds[1] :

            self.get_logger().info("turtle1 went out of boundary")
            self.service_client()

            
    def service_client(self):
        while self.client.wait_for_service(1) == False:
            self.get_logger().warn("Waiting for server")
        
        self.get_logger().warn("Server OK ..... Making a request")

        request = Empty.Request()
        future_obj = self.client.call_async(request)
        future_obj.add_done_callback(self.future_Callback)


    def future_Callback(self, future_done):
        self.get_logger().info("turtle1 has been reset.")



def main(args = None):

    rclpy.init(args=args)
    turtle_resetBoundary = my_node()
    rclpy.spin(turtle_resetBoundary)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
    




