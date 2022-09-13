#! /usr/bin/env python3

######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.12
# Topic: ROS2 Lab day 09
#
######################################################


import rclpy
from rclpy.node import Node

from example_interfaces.srv import SetBool
# example_interfaces/srv/SetBool.msg
# Raw Definition
# **request**
# #bool data # e.g. for hardware enabling / disabling
# ---
# **response**
# #bool success # indicate successful run of triggered service
# #string message # informational, e.g. for error messages

nodeName = "client_reset_counter"

class my_node(Node):
    def __init__(self):
        super().__init__(nodeName)
        self.client = self.create_client(SetBool, "srv_reset_counter")

        self.service_client()


    def service_client(self):
        while self.client.wait_for_service(0.25) == False:
            self.get_logger().info("Waiting for server to become ready")
        
        self.get_logger().warn("Server is OK.... Making a Request")
        
        
        ########
        # Note: This is closer to Trigger than SetBool
        # request.data is True ---> ie we are going to send data = true 
        # to server meaing
        ####
        # if the server recives request.data = true, it will reset its counter
        ########

        request = SetBool.Request()
        request.data = True

        future_obj = self.client.call_async(request)

        #add_done_callback adds a task to be executed when future is done
        future_obj.add_done_callback(self.future_callback)

    # i think future_done is future_obj ???
    def future_callback(self, future_done):
        
        self.get_logger().warn("Call_OK")

        response = future_done.result()

        if response.success == True:
            self.get_logger().info(f"Has the counter been reset? {response.success} ")
        elif response.success == False:
            self.get_logger().info(f"Has the counter been reset? {response.success} ")



def main(args=None):
    rclpy.init(args=args)
    client_reset_counter = my_node()
    rclpy.spin(client_reset_counter)
    rclpy.shutdown()

if __name__ == "__main__":
    main()