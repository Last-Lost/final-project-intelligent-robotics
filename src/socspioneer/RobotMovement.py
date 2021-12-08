#!/usr/bin/env python

import threading
from mapmover import MapMover
from AStar import AStar

class RobotMovementThread():

    def __init__(self, initial_state, goal_state, angle, direction, return_home):

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

            MapMover_object.map_mover([], self.rotate, 1)

        elif sector == 3:

            MapMover_object.map_mover([], self.rotate, 3)

        self.rotate = MapMover_object.getAngle()
        self.ini_direction = MapMover_object.getDirections()


    def move_robot(self):

        MapMover_object = MapMover()

        if self.return_home == True:

            MapMover_object1 = MapMover()
            MapMover_object1.map_mover(self.direction, self.rotate, 0)
            self.rotate = MapMover_object1.getAngle()


        elif self.goal_state[0] - self.goal_state[1] + 11 <= 0 and self.initial_state == (2,2):

            t1 = threading.Thread(target = self.AStarThread, args = ((-5, 6), ), daemon = True)

            t2 = threading.Thread(target = self.MapMoverThread, args = (MapMover_object, 1, ))

            t1.start()
            t2.start()

            t1.join()
            t2.join()

            for dir in self.direction:
                self.ini_direction.append(dir)

            MapMover_object1 = MapMover()
            MapMover_object1.map_mover(self.direction, self.rotate, 0)
            self.rotate = MapMover_object1.getAngle()

        elif self.goal_state[0] - self.goal_state[1] - 12 >= 0 and self.initial_state == (2,2):

            t1 = threading.Thread(target = self.AStarThread, args = ((7, -5), ), daemon = True)

            t2 = threading.Thread(target = self.MapMoverThread, args = (MapMover_object, 3, ))

            t1.start()
            t2.start()

            t1.join()
            t2.join()

            for dir in self.direction:
                self.ini_direction.append(dir)

            MapMover_object1 = MapMover()
            MapMover_object1.map_mover(self.direction, self.rotate, 0)
            self.rotate = MapMover_object1.getAngle()
            
        else:

            obj = AStar(self.initial_state, self.goal_state)

            obj.AStarPathPlanning()

            self.direction = obj.convert_path()

            MapMover_object1 = MapMover()
            MapMover_object1.map_mover(self.direction, self.rotate, 2)
            self.rotate = MapMover_object1.getAngle()

            self.ini_direction = self.direction

    
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
