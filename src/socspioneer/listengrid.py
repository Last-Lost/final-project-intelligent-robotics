#!/usr/bin/env python
import rospy
import numpy as np
from nav_msgs.msg import OccupancyGrid

def callbackGrid(msg):

    # print("w = ", (2 * (math.acos(msg.pose.pose.orientation.w)) * (180/math.pi)))

    # print(msg)
    # print(len(msg.data))
    count0 = 0
    count1 = 0
    count100 = 0
    for i in msg.data:
        if i == 0:
            count0 = count0 + 1 # Free pixels
        elif i == -1:
            count1 = count1 + 1 # Unknown pixels
        elif i <= 100:
            count100 = count100 + 1 # Boundry pixels

    data = np.array(msg.data).reshape((602, 602))

    # data = np.reshape(msg.data, (4000, 4000))

    counti = 0
    countj = 0

    for i in data[counti]:
        for j in data[counti][countj]:
            strin = ""
            if j == 0:
                print("0 ", counti, " , ", countj) # Free pixels
                strin = ("0 " + str(counti) + " , " + str(countj))
            elif j <= 100:
                print("1 ", counti, " , ", countj) # Boundry pixels
                strin = ("1 " + str(counti) + " , " + str(countj))
            elif j == -1:
                print("2 ", counti, " , ", countj) # Unknown pixels
                strin = ("2 " + str(counti) + " , " + str(countj))

            fileOdom = open("grid.txt", "a")
            fileOdom.write(strin)
            fileOdom.close()

            countj = countj + 1
        # print(counti, " , ", countj)
        counti = counti + 1

    
    print(count0, count1, count100)


    # fileOdom = open("odomdata.txt", "w")
    # fileOdom.close()

    # fileOdom = open("grid.txt", "w")
    # fileOdom.write(str(msg))
    # fileOdom.close()

def listengrid():

    rospy.init_node('MapInfo', anonymous=True)
    rospy.Subscriber("map", OccupancyGrid, callbackGrid)
    rospy.spin()

if __name__ == "__main__":
    try:
        listengrid()
    except:
        print("error inside listener.py main")
        pass
