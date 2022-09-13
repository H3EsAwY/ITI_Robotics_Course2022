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


nodeName = "node_client"
class my_node(Node):
	
	def __init__(self):
		super().__init__(nodeName)
		self.client = self.create_client(AddTwoInts, "add_two_ints")
		
		self.service_client(8,9)
		self.service_client(20,4)
		
	def service_client(self, a, b):
		while self.client.wait_for_service(timeout_sec = 0.25) == False:
			self.get_logger().warn("Waiting for service")
				
		req = AddTwoInts.Request()
		req.a = a
		req.b = b
		
		# the client makes a request asyncronously using call_async(request)
		# call_async returns a future that completes when the request is completed
		future_obj = self.client.call_async(req)
		
		#add_done_callback is imported from rclpy.task
		#add_done_callback(toBeCalled_when_future_completes) calls a function when future is competed
		#ie when the future_obj is completed 
		#future_obj is completed when the request is completed
		future_obj.add_done_callback(self.future_call)
		
		
	def future_call(self, future_response):
		self.get_logger().info(f" Result is: {future_response.result().sum}")
		
		
		
		
def main(args=None):

	rclpy.init(args=args)
	
	node_client = my_node()
	
	rclpy.spin(node_client)
	
	rclpy.shutdown()
	
if __name__ == "__main__":
	main()
		
		
		
		
		
		
