#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def get_direction_averages(ranges):

    left = ranges[:167]
    center = ranges[167:333]
    right = ranges[333:]
    left_avg = sum(left)/len(left)
    center_avg = sum(center)/len(center)
    right_avg = sum(right)/len(right)

    return left_avg, center_avg, right_avg


def findDirection(ranges, prev):

    direction = ""

    left_avg, center_avg, right_avg = get_direction_averages(ranges)

    max_avg = max(left_avg, center_avg, right_avg)

    if max_avg == left_avg:
        direction = "l"
    elif max_avg == center_avg:
        direction = "c"
    elif max_avg == right_avg:
        direction = "r"
    
    if center_avg <= 1:
        if prev == "l" and direction == "r":
            direction = "l"
        elif prev == "r" and direction == "l":
            direction = "r"
    elif left_avg <= 1:
        direction = "r"
    elif right_avg <= 1:
        direction = "l"
    elif prev == "l" and direction == "r" and center_avg > 1:
        direction = "c"
    elif prev == "r" and direction == "l" and center_avg > 1:
        direction = "c"

    return direction


def callbackLaser(msg):

    filereader = open("direction.txt", "r")
    prev_direction = filereader.read(1)
    filereader.close()

    direction = findDirection(msg.ranges, prev_direction)

    filewritter = open("direction.txt", "w")
    print(direction)
    filewritter.write(direction)
    filewritter.close()


def listener3():

    rospy.init_node('LaserData', anonymous=True)
    rospy.Subscriber("base_scan", LaserScan, callbackLaser)
    rospy.spin()


if __name__ == "__main__":
    try:
        listener3()
    except:
        print("error inside listener.py main")
        pass
