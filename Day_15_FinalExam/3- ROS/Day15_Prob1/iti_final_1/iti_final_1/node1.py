#! /usr/bin/env python3

######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.12
# Topic: ROS2 day 15 Final Exam Prob1 
#
######################################################

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

nodeName = "node1"

class my_node(Node):

    def __init__(self):
        super().__init__(nodeName)

        self.pub = self.create_publisher(String, "number", 10)

        timer_period = 1

        self.create_timer(timer_period, self.timerCallback)

        self.counter_alternating = 0


    def timerCallback(self):

        msg_string = String()

        if (self.counter_alternating%2) == 0:
            msg_string.data = "Add, 5"

        elif (self.counter_alternating%2) != 0:
            msg_string.data = "Add, 4"

        self.get_logger().info(f"{msg_string.data}")

        self.pub.publish(msg_string)

        self.counter_alternating += 1

    

def main(args=None):
	rclpy.init(args=args)
	
	node1 = my_node()
	
	rclpy.spin(node1)
	
	rclpy.shutdown()
	
if __name__ == "__main__":
	main()	

