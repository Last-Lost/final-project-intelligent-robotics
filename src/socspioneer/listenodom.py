#!/usr/bin/env python
import rospy
import math
from nav_msgs.msg import Odometry

def callbackOdom(msg):

    print("w = ", (2 * (math.acos(msg.pose.pose.orientation.w)) * (180/math.pi)))

    # fileOdom = open("odomdata.txt", "w")
    # fileOdom.close()

    # fileOdom = open("odomdata.txt", "w")
    # fileOdom.write(msg.twist.angular.z)
    # fileOdom.close()

def listenodom():

    rospy.init_node('OdomData', anonymous=True)
    rospy.Subscriber("odom", Odometry, callbackOdom)
    rospy.spin()

if __name__ == "__main__":
    try:
        listenodom()
    except:
        print("error inside listener.py main")
        pass

