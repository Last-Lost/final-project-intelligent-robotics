#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist

class MapMover:

    def __init__(self):

        self.directions = []
        self.rotate = 0


    def rotate_robot(self, pub, base_data, count, ore):

        if count == 10:

            base_data.angular.z = math.pi / 2

            for i in range(count):

                pub.publish(base_data)
                rospy.sleep(2/count)

            base_data.angular.z = 0
            pub.publish(base_data)
            rospy.sleep(0.01)

        elif ore == '+':

            base_data.angular.z = math.pi / 2

            for i in range(count):

                pub.publish(base_data)
                rospy.sleep(1/count)

            base_data.angular.z = 0
            pub.publish(base_data)
            rospy.sleep(0.01)


        elif ore  == '-':

            base_data.angular.z = -(math.pi / 2)

            for i in range(count):

                pub.publish(base_data)
                rospy.sleep(1/count)

            base_data.angular.z = 0
            pub.publish(base_data)
            rospy.sleep(0.01)


    def move_robot(self, pub, base_data):

            duration = 5
            base_data.linear.x = 0.05

            for i in range(duration):

                pub.publish(base_data)
                rospy.sleep(1 / duration)

            base_data.linear.x = 0
            pub.publish(base_data)


    def map_mover(self, path, initial_angle, sector):

        pub = rospy.Publisher("cmd_vel", Twist, queue_size = 1000)

        if sector == 0:

            directions = path

        elif sector == 1:

            filereader = open("sector1.txt", "r")
            directions = filereader.read().split("\n")
            filereader.close()

            rospy.sleep(5)

        elif sector == 2:

            directions = path

        elif sector == 3:

            filereader = open("sector3.txt", "r")
            directions = filereader.read().split("\n")
            filereader.close()

            rospy.sleep(5)

        rotate = initial_angle
        self.directions = directions

        for direction in directions:

            base_data = Twist()

            rospy.sleep(0.1)

            if direction == "t":

                if math.sin(rotate) ==  1:

                    self.move_robot(pub, base_data)

                elif math.cos(rotate) ==  1:
                    
                    self.rotate_robot(pub, base_data, 5, '+')
                    rotate = rotate + (math.pi/2)
                    self.move_robot(pub, base_data)

                elif math.sin(rotate) == -1:

                    self.rotate_robot(pub, base_data, 10, '+')
                    rotate = rotate + math.pi
                    self.move_robot(pub, base_data)

                elif math.cos(rotate) == -1:

                    self.rotate_robot(pub, base_data, 5, '-')
                    rotate = rotate - (math.pi/2)
                    self.move_robot(pub, base_data)

            elif direction == "r":
                
                if math.sin(rotate) ==  1:
                    
                    self.rotate_robot(pub, base_data, 5, '-')
                    rotate = rotate - (math.pi/2)
                    self.move_robot(pub, base_data)

                elif math.cos(rotate) ==  1:

                    self.move_robot(pub, base_data)

                elif math.sin(rotate) == -1:

                    self.rotate_robot(pub, base_data, 5, '+')
                    rotate = rotate + (math.pi/2)
                    self.move_robot(pub, base_data)

                elif math.cos(rotate) == -1:

                    self.rotate_robot(pub, base_data, 10, '+')
                    rotate = rotate + (math.pi)
                    self.move_robot(pub, base_data)

            elif direction == "b":
                
                if math.sin(rotate) ==  1:

                    self.rotate_robot(pub, base_data, 10, '+')
                    rotate = rotate + math.pi
                    self.move_robot(pub, base_data)

                elif math.cos(rotate) ==  1:
                    
                    self.rotate_robot(pub, base_data, 5, '-')
                    rotate = rotate - (math.pi/2)
                    self.move_robot(pub, base_data)

                elif math.sin(rotate) == -1:

                    self.move_robot(pub, base_data)

                elif math.cos(rotate) == -1:

                    self.rotate_robot(pub, base_data, 5, '+')
                    rotate = rotate + (math.pi/2)
                    self.move_robot(pub, base_data)

            elif direction == "l":

                if math.sin(rotate) ==  1:

                    self.rotate_robot(pub, base_data, 5, '+')
                    rotate = rotate  + (math.pi/2)
                    self.move_robot(pub, base_data)

                elif math.cos(rotate) == 1:

                    self.rotate_robot(pub, base_data, 10, '+')
                    rotate = rotate + (math.pi)
                    self.move_robot(pub, base_data)

                elif math.sin(rotate) == -1:

                    self.rotate_robot(pub, base_data, 5, '-')
                    rotate = rotate - (math.pi/2)
                    self.move_robot(pub, base_data)

                elif math.cos(rotate) == -1:

                    self.move_robot(pub, base_data)

        rospy.sleep(0.01)

        self.rotate = rotate

    
    def getAngle(self):

        return self.rotate

    
    def getDirections(self):

        return self.directions
