#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
# from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def get_direction_averages(ranges):

    left = ranges[:100]
    leftcenter = ranges[100:200]
    center = ranges[200:300]
    rightcenter = ranges[300:400]
    right = ranges[400:]
    left_avg = sum(left)/len(left)
    leftcenter_avg = sum(leftcenter)/len(leftcenter)
    center_avg = sum(center)/len(center)
    rightcenter_avg = sum(rightcenter)/len(rightcenter)
    right_avg = sum(right)/len(right)

    return left_avg, leftcenter_avg, center_avg, rightcenter_avg, right_avg


def findDirection(ranges, prev):

    direction = ""

    left_avg, leftcenter_avg, center_avg, rightcenter_avg, right_avg = get_direction_averages(ranges)

    min_avg = min(left_avg, leftcenter_avg, center_avg, rightcenter_avg, right_avg)
    max_avg = max(left_avg, leftcenter_avg, center_avg, rightcenter_avg, right_avg)

    if max_avg == left_avg:
        direction = "l"
    elif max_avg == leftcenter_avg:
        direction = "x"
    elif max_avg == center_avg:
        direction = "c"
    elif max_avg == rightcenter_avg:
        direction = "y"
    elif max_avg == right_avg:
        direction = "r"

    if min_avg == center_avg and center_avg <= 0.5:
        if prev == "l" and (direction == "y" or direction == "r"):
            direction = "l"
        elif prev == "x" and (direction == "y" or direction == "r"):
            direction = "x"
        elif prev == "y" and (direction == "x" or direction == "l"):
            direction = "y"
        elif prev == "r" and (direction == "x" or direction == "l"):
            direction = "r"
    elif min_avg == left_avg and left_avg <= 0.5:
        direction = "r"
    elif min_avg == leftcenter_avg and leftcenter_avg <= 0.5:
        direction = "y"
    elif min_avg == rightcenter_avg and rightcenter_avg <= 0.5:
        direction = "x"
    elif min_avg == right_avg and right_avg <= 0.5:
        direction = "l"
    elif prev == "l" and (direction == "y" or direction == "r"):
        direction = "l"
    elif prev == "x" and (direction == "y" or direction == "r"):
        direction = "x"
    elif prev == "y" and (direction == "x" or direction == "l"):
        direction = "y"
    elif prev == "r" and (direction == "x" or direction == "l"):
        direction = "r"

    return direction
    

def callback(msg):

    filereader = open("direction.txt", "r")
    prev_direction = filereader.read(1)
    filereader.close()

    direction = findDirection(msg.ranges, prev_direction)

    filewritter = open("direction.txt", "w")
    print(direction)
    filewritter.write(direction)
    filewritter.close()

    # file_alldirection = open("alldirection.txt", "a")
    # file_alldirection.write(direction)
    # file_alldirection.write("\n")
    # file_alldirection.close()

    # file = open("log.txt", "a")
    # file.write(f"{msg.ranges} \"\n\n\"")
    # file.close()


def listener5():

    rospy.init_node('LaserData', anonymous=True)
    rospy.Subscriber("base_scan", LaserScan, callback)
    rospy.spin()


if __name__ == "__main__":

    try:
        listener5()
    except:
        print("error inside listener.py main")
        pass
