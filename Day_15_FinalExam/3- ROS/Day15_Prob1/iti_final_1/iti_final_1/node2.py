#! /usr/bin/env python3

######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.21
# Topic: ROS2 day 15 Final Exam Prob1 
#
######################################################

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int64

nodeName = "node2"

class my_node(Node):
    def __init__(self):
        super().__init__(nodeName)

        self.pub = self.create_publisher(Int64, "accumulated_number", 10)
        self.create_subscription(String, "number", self.subCallback, 10 )

        self.counterAccum = 0


    def subCallback(self, msg):

        lst_data = msg.data.split(", ")

        num = int(lst_data[1])

        self.counterAccum += num

        msg_int64 = Int64()
        msg_int64.data = self.counterAccum
        
        self.pub.publish(msg_int64)
        self.get_logger().info(f"{msg_int64.data}")


def main(args=None):
	rclpy.init(args=args)
	
	node2 = my_node()
	
	rclpy.spin(node2)
	
	rclpy.shutdown()
	
if __name__ == "__main__":
	main()	
