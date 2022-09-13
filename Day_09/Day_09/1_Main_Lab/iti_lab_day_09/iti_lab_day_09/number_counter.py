#! /usr/bin/env python3

######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.12
# Topic: ROS2 Lab day 09
#
######################################################



from operator import truediv
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

from example_interfaces.srv import SetBool
# example_interfaces/srv/SetBool.msg
# Raw Definition
# **request**
# #bool data # e.g. for hardware enabling / disabling
# ---
# **response**
# #bool success # indicate successful run of triggered service
# #string message # informational, e.g. for error messages

nodeName = "number_counter"

class my_node(Node):

	def __init__(self):
		super().__init__(nodeName)
		
		self.create_subscription(Int64, "number", self.subCallback, 10)
		self.pub = self.create_publisher(Int64, "number_counter", 10)
		self.create_service(SetBool,"srv_reset_counter", self.srvCallback)

		self.counterAccum = 0

		self.get_logger().info("number_counter started")
		
		
	def subCallback(self, msg_int64):
		
		self.get_logger().info(f"iget data and counter is {self.counterAccum}")

		#accumulating the counter
		self.counterAccum = self.counterAccum + msg_int64.data

		msg_int64_counterAccum = Int64()
		msg_int64_counterAccum.data =  self.counterAccum
		self.pub.publish(msg_int64_counterAccum)

	def srvCallback(self, request, response):
		
		if request.data == True:
			self.counterAccum = 0
			response.success = True
			self.get_logger().info(f"Reset done, counter is {self.counterAccum}")
		
		return response

		
		
		
def main(args=None):

	rclpy.init(args=args)
	
	number_counter = my_node()
	
	rclpy.spin(number_counter)
	
	rclpy.shutdown()
	
	
if __name__ == "__main__":
	main()
		
		
		
		
		
		
