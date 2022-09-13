#! /usr/bin/env python3

######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.12
# Topic: ROS2 test day 09
#
######################################################



import rclpy
from rclpy.node import Node

from  example_interfaces.srv import AddTwoInts

nodeName = "node_server"
class my_node(Node):
	
	def __init__(self):
		super().__init__(nodeName)
		self.create_service(AddTwoInts, "add_two_ints", self.srvCallBack)
		
	def srvCallBack(self, request, response):
		
		response.sum = request.a + request.b
		
		self.get_logger().info(f"a: {request.a } + b: {request.b} = sum: {response.sum}  ")

		return response
		
		
		
def main(args=None):

	rclpy.init(args=args)
	
	node_server = my_node()
	
	rclpy.spin(node_server)
	
	rclpy.shutdown()
	
if __name__ == "__main__":
	main()
	
	
	
	
	
