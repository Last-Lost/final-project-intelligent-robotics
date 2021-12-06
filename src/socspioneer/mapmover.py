#!/usr/bin/env python
import time
import rospy
import math
from geometry_msgs.msg import Twist

def robot_rotations(pub, base_data, count, ore):

    # for i in range(count):

    #     print(i)

    #     if ore == '+':

    #         base_data.angular.z = (math.pi / 6 * 5)
    #         pub.publish(base_data)
    #         rospy.sleep(1)

    #     elif ore == '-':

    #         base_data.angular.z = -(math.pi / 6 * 5)
    #         pub.publish(base_data)
    #         rospy.sleep(1)

    #     print(i)

    if ore == '+':
        base_data.angular.z = math.pi / 2
        for i in range(count):
            # print(i)
            pub.publish(base_data)
            rospy.sleep(1/count)
        base_data.angular.z = 0
        pub.publish(base_data)

    elif ore  == '-':
        for i in range(count):
            base_data.angular.z = -(math.pi / 2)
            # print(i)
            pub.publish(base_data)
            rospy.sleep(1/count)
        base_data.angular.z = 0
        pub.publish(base_data)

def robot_movement(pub, base_data):

        duration = 5
        base_data.linear.x = 0.05

        for i in range(duration):
            pub.publish(base_data)
            rospy.sleep(1 / duration)

        base_data.linear.x = 0
        pub.publish(base_data)


def mapmover():

    pub = rospy.Publisher("cmd_vel", Twist, queue_size=5)
    rospy.init_node("Map_Mover", anonymous=True)
    # rate = rospy.Rate(10) # 10hz
    rate = 1

    filereader = open("sector1.txt", "r")
    directions = filereader.read().split("\n")
    directions.remove("")
    filereader.close()

    print(directions)

    rotate = 0

    # base_data = Twist()

    # rospy.sleep(1)

    # robot_rotations(pub, base_data, 6, "+")

    # base_data.linear.y = 0.5

    # pub.publish(base_data)

    # rospy.sleep(rate)

    # base_data = Twist()

    # count = 0

    # while not rospy.is_shutdown():

    for direction in directions:

        print(direction)

        base_data = Twist()

        rospy.sleep(0.01)

        # fileOdom = open("odomdata.txt", "r")
        # angle = fileOdom.read()
        # fileOdom.close()

        if direction == "t":

            if math.sin(rotate) ==  1:

                print("In t t")

                robot_movement(pub, base_data)
        
                # base_data.linear.x = 0.05
                # rotate = rotate + 0
                # pub.publish(base_data)
                # rospy.sleep(rate)

            elif math.cos(rotate) ==  1:

                print("In t r")
                
                robot_rotations(pub, base_data, 5, '+')
                # base_data.angular.z = - (math.pi/2)
                rotate = rotate + (math.pi/2)
                # pub.publish(base_data)
                # rospy.sleep(rate)
                # base_data = Twist()
                # base_data.linear.x =0.05
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)

            elif math.sin(rotate) == -1:

                print("In t b")

                robot_rotations(pub, base_data, 10, '+')
                # base_data.angular.z = (math.pi)
                rotate = rotate + math.pi
                # pub.publish(base_data)
                # rospy.sleep(rate)
                # base_data = Twist()
                # base_data.linear.x =0.05
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)

            elif math.cos(rotate) == -1:

                print("In t l")

                robot_rotations(pub, base_data, 5, '-')

                # base_data.angular.z = (math.pi/2)
                rotate = rotate - (math.pi/2)
                # pub.publish(base_data)
                # rospy.sleep(rate)
                # # base_data = Twist()
                # base_data.linear.x =0.05
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)

            else:
                print("didn't move")

        elif direction == "r":
            
            if math.sin(rotate) ==  1:

                print("In r t")
                
                robot_rotations(pub, base_data, 5, '-')

                # base_data.angular.z = (math.pi/2)
                rotate = rotate - (math.pi/2)
                # pub.publish(base_data)
                # rospy.sleep(rate)
                # base_data = Twist()
                # base_data.linear.x =0.05
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)
                
            elif math.cos(rotate) ==  1:

                print("In r r")

                # base_data.linear.x =0.05
                # rotate = rotate + 0
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)

            elif math.sin(rotate) == -1:

                print("In r b")

                robot_rotations(pub, base_data, 5, '+')
                # base_data.angular.z = - (math.pi/2)
                rotate = rotate + (math.pi/2)
                # pub.publish(base_data)
                # rospy.sleep(rate)
                # base_data = Twist()
                # base_data.linear.x =0.05
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)

            elif math.cos(rotate) == -1:

                print("In r l")

                robot_rotations(pub, base_data, 10, '+')
                # base_data.angular.z = (math.pi)
                rotate = rotate + (math.pi)
                # pub.publish(base_data)
                # rospy.sleep(rate)
                # base_data = Twist()
                # base_data.linear.x =0.05
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)

            else:
                print("didn't move")

        elif direction == "b":
            
            if math.sin(rotate) ==  1:

                print("In b t")

                robot_rotations(pub, base_data, 10, '+')
                # base_data.angular.z = (math.pi)
                rotate = rotate + math.pi
                # pub.publish(base_data)
                # rospy.sleep(rate)
                # base_data = Twist()
                # base_data.linear.x =0.05
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)

            elif math.cos(rotate) ==  1:

                print("In b r")
                
                robot_rotations(pub, base_data, 5, '-')
                # base_data.angular.z = (math.pi/2)
                rotate = rotate - (math.pi/2)
                # pub.publish(base_data)
                # rospy.sleep(rate)
                # base_data = Twist()
                # base_data.linear.x =0.05
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)

            elif math.sin(rotate) == -1:

                print("In b b")

                # base_data.linear.x =0.05
                # rotate = rotate + 0
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)

            elif math.cos(rotate) == -1:
                
                print("In b l")

                robot_rotations(pub, base_data, 5, '+')
                # base_data.angular.z = - (math.pi/2)
                rotate = rotate + (math.pi/2)
                # pub.publish(base_data)
                # rospy.sleep(rate)
                # base_data = Twist()
                # base_data.linear.x = 0.05
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)

            else:
                print("didn't move")

        elif direction == "l":

            if math.sin(rotate) ==  1:

                print("In l t")

                robot_rotations(pub, base_data, 5, '+')
                # base_data.angular.z = - (math.pi/2)
                rotate = rotate  + (math.pi/2)
                # pub.publish(base_data)
                # rospy.sleep(rate)
                # base_data = Twist()
                # base_data.linear.x =0.05
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)
                
            elif math.cos(rotate) == 1:

                print("In l r")

                robot_rotations(pub, base_data, 10, '+')
                # base_data.angular.z = (math.pi)
                rotate = rotate + (math.pi)
                # pub.publish(base_data)
                # rospy.sleep(rate)
                # base_data = Twist()
                # base_data.linear.x =0.05
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)

            elif math.sin(rotate) == -1:

                print("In l b")

                robot_rotations(pub, base_data, 5, '-')
                # base_data.angular.z = (math.pi/2)
                rotate = rotate - (math.pi/2)
                # pub.publish(base_data)
                # rospy.sleep(rate)
                # base_data = Twist()
                # base_data.linear.x =0.05
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)

            elif math.cos(rotate) == -1:

                print("In l l")

                # base_data.linear.x =0.05
                # rotate = rotate + 0
                # pub.publish(base_data)
                # rospy.sleep(rate)

                robot_movement(pub, base_data)

            else:
                print("didn't move")

        else:
            print("did not work " + direction + " char")

        print(rotate, "\n")

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

    # robot_rotations(pub, base_data, 11)

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
    

if __name__ == "__main__":

    try:
        mapmover()
    except rospy.ROSInterruptException:

        print("did not work")
        pass
