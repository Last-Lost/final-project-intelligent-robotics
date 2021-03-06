#!/usr/bin/env python

import rospy
import numpy as np
from nav_msgs.msg import OccupancyGrid

def callbackGrid(msg):

    count0 = 0
    count1 = 0
    count2 = 0

    index = 0
    counti = 0
    countj = 0

    for i in msg.data:

        if i == 0:
            count0 = count0 + 1 # Free pixels
            strin = (str(counti) + " " + str(countj) + " 0")
        elif i == 100:
            count1 = count1 + 1 # Boundry pixels
            strin = (str(counti) + " " + str(countj) + " 1")
        elif i == -1:
            count2 = count2 + 1 # Unknown pixels
            strin = (str(counti) + " " + str(countj) + " 2")
        
        fileOdom = open("grid.txt", "a")
        fileOdom.write(strin + "\n")
        fileOdom.close()

        index = index + 1
        countj = countj + 1

        if countj == 602:
            countj = 0
            counti = counti + 1

    data = msg.data

    filewriter = open("map_data.txt", "w")
    filewriter.write(str(data))
    filewriter.close()


def listengrid():

    rospy.init_node('MapInfo', anonymous=True)
    rospy.Subscriber("map", OccupancyGrid, callbackGrid)
    rospy.spin()
    

if __name__ == "__main__":
    try:
        listengrid()
    except:
        print("error inside listengrid.py main")
        pass
