#! /usr/bin/env python3

######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.11
# Topic: ROS2Lab day 08
#
##########################
#
#"box_turtule" tasks:
#	*subscribe to turtule postion topic --> pose
#	if turtule tries to exceed x =6 ot y =6 stop it --> cmd_vel zero
#
#	*publish new cmd_vel to stop turtule
#
######################################################


import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist,Vector3


nodeName = "node_box_turtle"

class my_Node(Node):
	def __init__(self):
		super().__init__(nodeName)
		
		self.pub = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
		self.create_subscription(Pose, "turtle1/pose", self.subCallBack, 10)
		
		self.xBoundary = 6
		self.yBoundary = 6
		
	def subCallBack(self, msg_pose):
	
		if msg_pose.x >= self.xBoundary or msg_pose.y>= self.yBoundary:
		
			msg_twist = Twist()
			
			#msg_twist.linear is of type Vector3 and has 3 objects of type float, x y z
			
			vector3_velocity = Vector3()
			vector3_velocity.x = 0.0
			vector3_velocity.y = 0.0
			vector3_velocity.z = 0.0
			
			msg_twist.linear = vector3_velocity
			
			self.pub.publish(msg_twist)
		

def main(args=None):
	
	rclpy.init(args=args)
	
	node_box_turtle = my_Node()
	
	rclpy.spin(node_box_turtle)
	
	rcply.shutdown()
	
if __name__ == "__main__":
	main()

