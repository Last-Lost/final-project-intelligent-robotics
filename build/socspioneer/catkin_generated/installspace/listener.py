#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

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


def findDirection(ranges):

    left_avg, leftcenter_avg, center_avg, rightcenter_avg, right_avg = get_direction_averages(ranges)

    min_avg = min(left_avg, leftcenter_avg, center_avg, rightcenter_avg, right_avg)
    max_avg = max(left_avg, leftcenter_avg, center_avg, rightcenter_avg, right_avg)

    # if (center_avg >= 0.5) and (max_avg != center_avg):
    #     return "c"
    if min_avg <= 0.5:
        if left_avg == min_avg:
            return "r"
        elif leftcenter_avg == min_avg:
            return "y"
        elif center_avg == min_avg:
            if max_avg == left_avg:
                return "l"
            elif max_avg == leftcenter_avg:
                return "x"
            elif max_avg == center_avg:
                return "c"
            elif max_avg == rightcenter_avg:
                return "y"
            elif max_avg == right_avg:
                return "r"
        elif rightcenter_avg == min_avg:
            return "x"
        elif right_avg == min_avg:
            return "l"

    if max_avg == left_avg:
        return "l"
    elif max_avg == leftcenter_avg:
        return "x"
    elif max_avg == center_avg:
        return "c"
    elif max_avg == rightcenter_avg:
        return "y"
    elif max_avg == right_avg:
        return "r"


def callback(msg):

    direction = findDirection(msg.ranges)
    filewritter = open("direction.txt", "w")
    print(direction)
    filewritter.write(direction)
    filewritter.close()

    file_alldirection = open("alldirection.txt", "a")
    file_alldirection.write(direction)
    file_alldirection.write("\n")
    file_alldirection.close()

    # file = open("log.txt", "a")
    # file.write(f"{msg.ranges} \"\n\n\"")
    # file.close()


def listener():
    # rospy.init_node("scan_values", anonymous=True)
    # laser_data = LaserScan()
    # rospy.Subscriber("base_scan", laser_data, callback)
    # rospy.spin()

    rospy.init_node('LaserData', anonymous=True)
    rospy.Subscriber("base_scan", LaserScan, callback) 
    rospy.spin()


if __name__ == "__main__":
    try:
        listener()
    except:
        print("error inside listener.py main")
        pass
