#!/usr/bin/env python

import math
import threading
from mapmover import MapMover
from AStar import AStar

class RobotMovementThread():

    def __init__(self, initial_state, goal_state, angle, direction, return_home):

        # print("I am being called")

        self.initial_state = initial_state
        self.goal_state = goal_state
        self.rotate = angle
        self.direction = direction
        self.ini_direction = []
        self.return_home = return_home


    def AStarThread(self, current_state):

        obj = AStar(current_state, self.goal_state)
        obj.AStarPathPlanning()
        direction = obj.convert_path()
        self.direction = direction


    def MapMoverThread(self, MapMover_object, sector):

        if sector == 1:

            # MapMover_object = MapMover()
            MapMover_object.map_mover([], self.rotate, 1)

        elif sector == 3:

            # MapMover_object = MapMover()
            MapMover_object.map_mover([], self.rotate, 3)

        self.rotate = MapMover_object.getAngle()
        self.ini_direction = MapMover_object.getDirections()


    def move_robot(self):

        MapMover_object = MapMover()

        if self.return_home == True:

            MapMover_object1 = MapMover()
            MapMover_object1.map_mover(self.direction, self.rotate, 0)
            self.rotate = MapMover_object1.getAngle()


        elif self.goal_state[0] - self.goal_state[1] + 11 <= 0:

            # print("sector 1")

            t1 = threading.Thread(target = self.AStarThread, args = ((-5, 6), ), daemon = True)

            t2 = threading.Thread(target = self.MapMoverThread, args = (MapMover_object, 1, ))

            t1.start()

            # print("Thread 1 Started")

            t2.start()

            # print("Thread 2 Started")

            # rotate = mapmover([], -(math.pi/2), 1)

            t1.join()
            t2.join()

            for dir in self.direction:
                self.ini_direction.append(dir)

            MapMover_object1 = MapMover()
            MapMover_object1.map_mover(self.direction, self.rotate, 0)
            self.rotate = MapMover_object1.getAngle()

            # rotate = mapmover(self.direction, rotate, 0)

        elif self.goal_state[0] - self.goal_state[1] - 12 >= 0:

            # print("sector 3")

            t1 = threading.Thread(target = self.AStarThread, args = ((7, -5), ), daemon = True)

            t2 = threading.Thread(target = self.MapMoverThread, args = (MapMover_object, 3, ))

            t1.start()

            # print("Thread Started")

            t2.start()

            # print("Thread 2 Started")

            # rotate = mapmover([], -(math.pi/2), 3)

            t1.join()
            t2.join()

            for dir in self.direction:
                self.ini_direction.append(dir)

            MapMover_object1 = MapMover()
            MapMover_object1.map_mover(self.direction, self.rotate, 0)
            self.rotate = MapMover_object1.getAngle()

            # rotate = mapmover(self.direction, rotate, 0)
            
        else:

            # print("sector 2")

            obj = AStar(self.initial_state, self.goal_state)

            obj.AStarPathPlanning()

            self.direction = obj.convert_path()

            MapMover_object1 = MapMover()
            MapMover_object1.map_mover(self.direction, self.rotate, 2)
            self.rotate = MapMover_object1.getAngle()

            self.ini_direction = self.direction

            # rotate = mapmover(direction, -(math.pi/2), 2)

    
    def getDirections(self):

        return self.ini_direction


    def getAngle(self):

        return self.rotate


def main():

    obj = RobotMovementThread((2, 2), (10.25, -6.9), [], False)
    obj.move_robot()


if __name__ == "__main__":

    try:

        main()

    except Exception as err:

        print(err)
