#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist

class MapMover:

    def __init__(self):

        # rospy.init_node("Map_Mover", anonymous=True)

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

        # rospy.init_node("Map_Mover", anonymous=True)

        # rate = rospy.Rate(10) # 10hz
        # rate = 1

        if sector == 0:

            # print(sector)

            directions = path

        elif sector == 1:

            # print(sector)

            filereader = open("sector1.txt", "r")
            directions = filereader.read().split("\n")
            # directions.remove("")
            filereader.close()

            rospy.sleep(5)

        elif sector == 2:

            # print(sector)

            directions = path

        elif sector == 3:

            # print(sector)

            filereader = open("sector3.txt", "r")
            directions = filereader.read().split("\n")
            # directions.remove("")
            filereader.close()

            rospy.sleep(5)

        # print(directions, "\n")

        rotate = initial_angle
        self.directions = directions

        for direction in directions:

            base_data = Twist()

            rospy.sleep(0.1)

            if direction == "t":

                if math.sin(rotate) ==  1:

                    # print("In t t")

                    self.move_robot(pub, base_data)
            
                    # base_data.linear.x = 0.05
                    # rotate = rotate + 0
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                elif math.cos(rotate) ==  1:

                    # print("In t r")
                    
                    self.rotate_robot(pub, base_data, 5, '+')
                    rotate = rotate + (math.pi/2)
                    self.move_robot(pub, base_data)

                    # base_data.angular.z = - (math.pi/2)
                    # pub.publish(base_data)
                    # rospy.sleep(rate)
                    # base_data = Twist()
                    # base_data.linear.x =0.05
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                elif math.sin(rotate) == -1:

                    # print("In t b")

                    self.rotate_robot(pub, base_data, 10, '+')
                    rotate = rotate + math.pi
                    self.move_robot(pub, base_data)

                    # base_data.angular.z = (math.pi)
                    # pub.publish(base_data)
                    # rospy.sleep(rate)
                    # base_data = Twist()
                    # base_data.linear.x =0.05
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                elif math.cos(rotate) == -1:

                    # print("In t l")

                    self.rotate_robot(pub, base_data, 5, '-')
                    rotate = rotate - (math.pi/2)
                    self.move_robot(pub, base_data)

                    # base_data.angular.z = (math.pi/2)
                    # pub.publish(base_data)
                    # rospy.sleep(rate)
                    # # base_data = Twist()
                    # base_data.linear.x =0.05
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                # else:
                #     print("didn't move")

            elif direction == "r":
                
                if math.sin(rotate) ==  1:

                    # print("In r t")
                    
                    self.rotate_robot(pub, base_data, 5, '-')
                    rotate = rotate - (math.pi/2)
                    self.move_robot(pub, base_data)

                    # base_data.angular.z = (math.pi/2)
                    # pub.publish(base_data)
                    # rospy.sleep(rate)
                    # base_data = Twist()
                    # base_data.linear.x =0.05
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                elif math.cos(rotate) ==  1:

                    # print("In r r")

                    self.move_robot(pub, base_data)

                    # base_data.linear.x =0.05
                    # rotate = rotate + 0
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                elif math.sin(rotate) == -1:

                    print("In r b")

                    self.rotate_robot(pub, base_data, 5, '+')
                    rotate = rotate + (math.pi/2)
                    self.move_robot(pub, base_data)

                    # base_data.angular.z = - (math.pi/2)
                    # pub.publish(base_data)
                    # rospy.sleep(rate)
                    # base_data = Twist()
                    # base_data.linear.x =0.05
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                elif math.cos(rotate) == -1:

                    # print("In r l")

                    self.rotate_robot(pub, base_data, 10, '+')
                    rotate = rotate + (math.pi)
                    self.move_robot(pub, base_data)

                    # base_data.angular.z = (math.pi)
                    # pub.publish(base_data)
                    # rospy.sleep(rate)
                    # base_data = Twist()
                    # base_data.linear.x =0.05
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                # else:
                #     print("didn't move")

            elif direction == "b":
                
                if math.sin(rotate) ==  1:

                    # print("In b t")

                    self.rotate_robot(pub, base_data, 10, '+')
                    rotate = rotate + math.pi
                    self.move_robot(pub, base_data)

                    # base_data.angular.z = (math.pi)
                    # pub.publish(base_data)
                    # rospy.sleep(rate)
                    # base_data = Twist()
                    # base_data.linear.x =0.05
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                elif math.cos(rotate) ==  1:

                    # print("In b r")
                    
                    self.rotate_robot(pub, base_data, 5, '-')
                    rotate = rotate - (math.pi/2)
                    self.move_robot(pub, base_data)

                    # base_data.angular.z = (math.pi/2)
                    # pub.publish(base_data)
                    # rospy.sleep(rate)
                    # base_data = Twist()
                    # base_data.linear.x =0.05
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                elif math.sin(rotate) == -1:

                    # print("In b b")

                    self.move_robot(pub, base_data)

                    # base_data.linear.x =0.05
                    # rotate = rotate + 0
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                elif math.cos(rotate) == -1:
                    
                    # print("In b l")

                    self.rotate_robot(pub, base_data, 5, '+')
                    rotate = rotate + (math.pi/2)
                    self.move_robot(pub, base_data)

                    # base_data.angular.z = - (math.pi/2)
                    # pub.publish(base_data)
                    # rospy.sleep(rate)
                    # base_data = Twist()
                    # base_data.linear.x = 0.05
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                # else:
                #     print("didn't move")

            elif direction == "l":

                if math.sin(rotate) ==  1:

                    # print("In l t")

                    self.rotate_robot(pub, base_data, 5, '+')
                    rotate = rotate  + (math.pi/2)
                    self.move_robot(pub, base_data)

                    # base_data.angular.z = - (math.pi/2)
                    # pub.publish(base_data)
                    # rospy.sleep(rate)
                    # base_data = Twist()
                    # base_data.linear.x =0.05
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                elif math.cos(rotate) == 1:

                    # print("In l r")

                    self.rotate_robot(pub, base_data, 10, '+')
                    rotate = rotate + (math.pi)
                    self.move_robot(pub, base_data)

                    # base_data.angular.z = (math.pi)
                    # pub.publish(base_data)
                    # rospy.sleep(rate)
                    # base_data = Twist()
                    # base_data.linear.x =0.05
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                elif math.sin(rotate) == -1:

                    # print("In l b")

                    self.rotate_robot(pub, base_data, 5, '-')
                    rotate = rotate - (math.pi/2)
                    self.move_robot(pub, base_data)

                    # base_data.angular.z = (math.pi/2)
                    # pub.publish(base_data)
                    # rospy.sleep(rate)
                    # base_data = Twist()
                    # base_data.linear.x =0.05
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                elif math.cos(rotate) == -1:

                    # print("In l l")

                    self.move_robot(pub, base_data)

        rospy.sleep(0.01)

        self.rotate = rotate

        # return rotate

    
    def getAngle(self):

        return self.rotate

    
    def getDirections(self):

        return self.directions

                    # base_data.linear.x =0.05
                    # rotate = rotate + 0
                    # pub.publish(base_data)
                    # rospy.sleep(rate)

                # else:
                #     print("didn't move")

            # else:
            #     print("did not work " + direction + " char")

            # print("\n")

        # duration = 10

        # base_data = Twist()

        # rospy.sleep(0.01)

        # self.rotate_robot(pub, base_data, 10, "+")

        # duration = 5
        # base_data.linear.x = 0.05
        # for i in range(duration):
        #     pub.publish(base_data)
        #     rospy.sleep(1 / duration)


        # base_data.linear.x = 0
        # pub.publish(base_data)

        #     time.sleep(1)

            # 

            # base_data = Twist()
            # base_data.linear.x =0.5
            # # rotate = rotate + 0
            # pub.publish(base_data)
            # rospy.sleep(rate)

            # time.sleep(1)

            # # pub.publish(base_data)
            # # rospy.sleep(rate)

        # base_data = Twist()
        # base_data.angular.z = math.pi / 6 * 5 
        # pub.publish(base_data)
        # rospy.sleep(rate)
        # # base_data = Twist()
        # base_data.angular.z = math.pi / 6 * 5
        # pub.publish(base_data)
        # rospy.sleep(rate)
        # # base_data = Twist()
        # base_data.angular.z = math.pi / 6 * 5
        # pub.publish(base_data)
        # rospy.sleep(rate)
        # # base_data = Twist()
        # base_data.angular.z = math.pi / 6 * 5 
        # pub.publish(base_data)
        # rospy.sleep(rate)
        # # base_data = Twist()
        # base_data.angular.z = math.pi / 6 * 5 
        # pub.publish(base_data)
        # rospy.sleep(rate)
        # # base_data = Twist()
        # base_data.angular.z = math.pi / 6 * 5 
        # pub.publish(base_data)

        # self.rotate_robot(pub, base_data, 11)

            # base_data = Twist()
            # base_data.angular.z = math.pi / 10 
            # pub.publish(base_data)
            # base_data = Twist()
            # base_data.angular.z = math.pi / 10
            # pub.publish(base_data)
            # base_data = Twist()
            # base_data.angular.z = math.pi / 10 
            # pub.publish(base_data)
            # base_data = Twist()
            # base_data.angular.z = math.pi / 10 
            # pub.publish(base_data)

        # duration = 10
        # base_data.angular.z = math.pi / 2
        # for i in range(duration):
        #     pub.publish(base_data)
        #     rospy.sleep(0.25)
        
        # base_data.angular.z = 0
        # pub.publish(base_data)

        # pub.publish(base_data)
        # rospy.sleep(duration)
        # base_data.angular.z = 0
        # pub.publish(base_data)
            
            # base_data = Twist()
            # base_data.angular.z = math.pi / 10
            # pub.publish(base_data)
            # base_data = Twist()
            # base_data.angular.z = math.pi / 2 / 6
            # pub.publish(base_data)
            # base_data = Twist()
            # base_data.angular.z = math.pi / 2 / 6
            # pub.publish(base_data)

        # rospy.sleep(rate)

            # count+= 1

            # print(count)

            # base_data = Twist()
            # base_data.angular.z = (math.pi / 2)
            # pub.publish(base_data)
            # rospy.sleep(rate)
            # base_data = Twist()
            # base_data.angular.z = (math.pi / 2)
            # pub.publish(base_data)
            # rospy.sleep(rate)
            # base_data = Twist()
            # base_data.angular.z = (math.pi / 2)
            # pub.publish(base_data)
            # rospy.sleep(rate)
            # base_data = Twist()
            # base_data.angular.z = (math.pi / 2)
            # pub.publish(base_data)
            # rospy.sleep(rate)

        # time.sleep(1)

        

    # if __name__ == "__main__":

    #     try:
    #         mapmover()
    #     except rospy.ROSInterruptException:

    #         print("did not work")
    #         pass
