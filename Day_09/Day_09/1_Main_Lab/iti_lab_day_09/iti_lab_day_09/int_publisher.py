#! /usr/bin/env python3

######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.12
# Topic: ROS2Lab day 09
#
######################################################

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64



nodeName = "int_publisher"

class my_node(Node):
	def __init__(self):
		super().__init__(nodeName)
		
		self.pub = self.create_publisher(Int64, "number", 10)
		
		timer_period = 1
		
		self.create_timer(timer_period,self.timerCallBack)
		

	def timerCallBack(self):
		
		msg_int64 = Int64()
		
		msg_int64.data = 5
		
		self.pub.publish(msg_int64)
		
		self.get_logger().info(str(msg_int64.data))
		
		
def main(args=None):
	rclpy.init(args=args)
	
	int_publisher = my_node()
	
	rclpy.spin(int_publisher)
	
	rclpy.shutdown()
	
if __name__ == "__main__":
	main()	











			
