#! /usr/bin/env python3

######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.08
# Topic: ROS2Lab day 07
######################################################

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from std_msgs.msg import Bool

class my_node2(Node):

	def __init__(self):
	
		super().__init__("number_counter")
		
		self.pub = self.create_publisher(Bool, "reset_flag", 10)
		
		self.subscription  = self.create_subscription(String, "str_topic", self.node2_SubCallback, 10)
		
		
	def node2_SubCallback(self, msg):
		
		
		print(f"{msg.data}")
		 
		lstExtractInt = [int(char) for char in msg.data if char.isdigit()]
		
		if lstExtractInt[0] == 5:
		
			msgResetFLag = Bool()
			msgResetFLag.data = True
			self.pub.publish(msgResetFLag)
			
			
		#elif lstExtractInt[0] < 5:
			#msgResetFLag = Bool()
			#msgResetFLag.data = Flase
			#self.pub.publish(msgResetFLag)
				
				
			
def main(args=None):
	rclpy.init(args=args)

	node2 = my_node2()
		
	rclpy.spin(node2)
	
	rclpy.shutdown()
		
if __name__ == "__main__":
	main()				
				
