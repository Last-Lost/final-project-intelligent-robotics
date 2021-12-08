#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist

def changeAngle(initial_angle):

    pub = rospy.Publisher("cmd_vel", Twist, queue_size = 1000)
    # rospy.init_node("Change_Angle", anonymous=True)

    base_data = Twist()

    if initial_angle == math.pi / 4:
        count = 5
        ore = '+'
    elif initial_angle == -(math.pi / 4):
        count = 5
        ore = '-'
    elif initial_angle == 3* (math.pi / 4):
        count = 15
        ore = '+'
    elif initial_angle == -(3*(math.pi / 4)):
        count = 15
        ore = '-'

    base_data.angular.z = math.pi / 2

    rospy.sleep(0.1)

    if ore == '+':

        base_data.angular.z = (2 * math.pi / 8)

        for i in range(count):

            pub.publish(base_data)
            rospy.sleep(1)

        base_data.angular.z = 0
        pub.publish(base_data)
        rospy.sleep(0.01)

    elif ore  == '-':

        base_data.angular.z = -(2 * math.pi / 8)

        for i in range(count):

            pub.publish(base_data)
            rospy.sleep(1)

        base_data.angular.z = 0
        pub.publish(base_data)
        rospy.sleep(0.01)

# changeAngle(3*(math.pi/4))


