#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist

def mapmover():

    pub = rospy.Publisher("cmd_vel", Twist, queue_size=100)
    rospy.init_node("Map_Mover", anonymous=True)
    rate = rospy.Rate(20) # 10hz

    while not rospy.is_shutdown():

        base_data = Twist()

        filereader = open("direction.txt", "r")
        direction = filereader.read(1)
        filereader.close()

        if direction == "l":
            base_data.angular.z = -(math.pi/5)
        elif direction == "c":
            base_data.linear.x = 0.2
        elif direction == "r":
            base_data.angular.z = (math.pi/5)

        pub.publish(base_data)
        rate.sleep()


if __name__ == "__main__":

    try:
        mapmover()
    except rospy.ROSInterruptException:
        pass
