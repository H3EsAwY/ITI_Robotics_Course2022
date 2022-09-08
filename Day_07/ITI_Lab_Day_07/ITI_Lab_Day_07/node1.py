#! /usr/bin/env python3

######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.08
# Topic: ROS2Lab day 07
#
##########################
#
# node1 (str_publisher) tasks:
#
# 	publish "str_topic" --> (“ <your name> is publish <,><counter>”) and update the counter every 1 second
#	subscribe to "reset_flag"
#
##########################
# 
# node2 ("number_counter") tasks:
#
#	subscribe to  "str_topic"
#	publish "reset_flag" --> is set to True when the counter from node1 reaches a value of 5
#
######################################################


import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from std_msgs.msg import Bool

class my_node1(Node):
	
	def __init__(self):
		super().__init__("str_publisher")
		
		self.counter = 0
		self.Globalcounter = 0
		timer_period = 1
		
		
		self.create_timer(timer_period, self.timerCallback)
		
		self.pub = self.create_publisher(String, "str_topic", 10)

		self.sub = self.create_subscription(Bool, "reset_flag", self.node1_SubCallback,10)
		
		
	def timerCallback(self):
		
		str_msg = String()
		
		str_msg.data = f"Hany Elesawy is publishing... , {self.counter}"
		self.pub.publish(str_msg)
		
		print(f"Node 1 publish tick {self.Globalcounter}")
		
		self.counter += 1
		self.Globalcounter += 1
		
		
	def node1_SubCallback(self, msg):
		
		if msg.data == True: 					#if resetflag == true --> reset 
			self.counter = 0
		
		
def main(args=None):

	rclpy.init(args=args)
	
	node1 = my_node1()
		
	rclpy.spin(node1)

	rclpy.shutdown()
		
if __name__ == "__main__":
	main()
		
