#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry

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

    min_avg = min(left_avg, center_avg, right_avg)
    max_avg = max(left_avg, center_avg, right_avg)


    # if (center_avg >= 0.5) and (max_avg != center_avg):
    #     return "c"

    # if min_avg <= 0.5:
    #     if left_avg == min_avg:
    #         return "r"
    #     elif leftcenter_avg == min_avg:
    #         return "y"
    #     elif center_avg == min_avg:
    #         if max_avg == left_avg:
    #             return "l"
    #         elif max_avg == leftcenter_avg:
    #             return "x"
    #         elif max_avg == center_avg:
    #             return "c"
    #         elif max_avg == rightcenter_avg:
    #             return "y"
    #         elif max_avg == right_avg:
    #             return "r"
    #     elif rightcenter_avg == min_avg:
    #         return "x"
    #     elif right_avg == min_avg:
    #         return "l"
     
    # if left_avg <= 1:
    #     if center_avg > 1:
    #         direction = "c"
    #     else:
    #         direction = "r"
    # elif right_avg <= 1:
    #     if center_avg > 1:
    #         direction = "c"
    #     else:
    #         direction = "l"
    # elif center_avg <= 1:
    #     if prev == "c":
    #         if left_avg > right_avg:
    #             direction = "l"
    #         else:
    #             direction = "r"
    #     else:
    #         direction = prev
    # elif center_avg == min_avg:
    #     if max_avg == left_avg:
    #         direction = "l"
    #     else:
    #         direction = "r"
    # elif center_avg != min_avg or center_avg > 1:
    #     direction = "c"

    # if prev == "l" and direction == "r":
    #     direction = "r"
    # elif prev == "r" and direction == "l":
    #     direction = "l"

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

    # fileOdom = open("odomdata.txt", "r")
    # angle = fileOdom.read()
    # fileOdom.close()

    # if len(angle) != 0:
    #     print(angle)
    #     if angle[0] == "-":
    #         if direction == "r":
    #             direction = "l"
    #         elif direction == "l":
    #             direction = "r"
    # else:
    #     print("empty")



    # if max_avg == left_avg:
    #     direction = "l"
    # elif max_avg == center_avg:
    #     direction = "c"
    #     return direction
    # elif max_avg == right_avg:
    #     direction = "r"

    # if center_avg == min_avg or center_avg != max_avg:
    #     if prev == "l" and direction == "r":
    #         return "l"
    #     elif prev == "r" and direction == "l":
    #         return "r"

    return direction


# def callbackOdom(msg):

#     fileOdom = open("odomdata.txt", "w")
#     fileOdom.close()

#     fileOdom = open("odomdata.txt", "w")
#     print(msg.twist.twist.angular.z)
#     fileOdom.write(str(msg.twist.twist.angular.z))
#     fileOdom.close()


def callbackLaser(msg):

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


def listener3():
    # rospy.init_node("scan_values", anonymous=True)
    # laser_data = LaserScan()
    # rospy.Subscriber("base_scan", laser_data, callback)
    # rospy.spin()

    rospy.init_node('LaserData', anonymous=True)
    # rospy.Subscriber("odom", Odometry, callbackOdom)
    rospy.Subscriber("base_scan", LaserScan, callbackLaser)
    rospy.spin()


if __name__ == "__main__":
    try:
        listener3()
    except:
        print("error inside listener.py main")
        pass
