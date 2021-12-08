#!/usr/bin/env python

import numpy as np

class AStar:

    def __init__(self, initial_pair, goal_pair):

        self.grid_dict = self.readgrid()
        self.initial_pair = initial_pair
        self.goal_pair = goal_pair
        self.path = []


    def readgrid(self):

        grid_dict = {}
        filereader = open("grid.txt", "r")
        grids = filereader.read().split("\n")
        filereader.close()

        for grid in grids:
            if grid != "":
                string = grid.split(" ")
                grid_dict.update({(int(string[0]), int(string[1])) : int(string[2])})

        grid_array = []

        for key, value in grid_dict.items():
            grid_array.append(value)

        data = np.array(grid_array)

        reshape_data = np.reshape(data, (602, 602))

        trans_data = np.transpose(reshape_data)

        rot_data = np.rot90(trans_data)

        counti = 0
        countj = 0

        dict_data = {}

        for i in range(602*602):

            dict_data.update({(counti, countj) : rot_data[counti][countj]})
            countj = countj + 1

            if countj == 602:
                countj = 0
                counti = counti + 1

        return dict_data


    def shift_to_origin(self, pair):

        X = 300 - pair[1]*20
        Y = pair[0]*20 + 300

        Pair = (X, Y)

        return Pair


    def shift_from_origin(self, pair):

        X = -(300 - pair[1])/20
        Y = -(pair[0] - 300)/20

        Pair = (X, Y)

        return Pair


    def find_direction(self, node):

        xDiff = node[0][0] - node[1][0]
        yDiff = node[0][1] - node[1][1]

        direction = ""

        if yDiff > 0:
            direction = "t"
        elif xDiff > 0:
            direction = "r"
        elif yDiff < 0:
            direction = "b"
        elif xDiff < 0:
            direction = "l"
        else:
            direction = "N"
        
        return direction


    def check_for_block(self, current_pair):

        nodes = []

        for i in range(5):

            nodes.append((current_pair[0], current_pair[1] - (i + 1)))
            nodes.append((current_pair[0] + i + 1, current_pair[1]))
            nodes.append((current_pair[0], current_pair[1] + i + 1))
            nodes.append((current_pair[0] - (i + 1), current_pair[1]))

        for i in range(3):

            nodes.append((current_pair[0] + i + 1, current_pair[1] + i + 1))
            nodes.append((current_pair[0] - (i + 1), current_pair[1] + i + 1))
            nodes.append((current_pair[0] + i + 1, current_pair[1] - (i + 1)))
            nodes.append((current_pair[0] - (i + 1), current_pair[1] - (i + 1)))


        for node in nodes:

            if self.grid_dict[node] == 1:
                return False

        return True

    
    def find_neighbours(self, current_pair, count, prev):

        possiblePoints = []

        current_pair = self.shift_to_origin(current_pair)
        prev_pair = self.shift_to_origin(prev)

        xDiff = current_pair[0] - prev_pair[0]
        yDiff = current_pair[1] - prev_pair[1]

        direction = ""

        if yDiff > 0:
            direction = "t"
        elif xDiff > 0:
            direction = "r"
        elif yDiff < 0:
            direction = "b"
        elif xDiff < 0:
            direction = "l"
        else:
            direction = "N"

        for key, value in self.grid_dict.items():

            if current_pair[0] == key[0] and (current_pair[1] + 1) == key[1] and direction != "b" and self.check_for_block((current_pair[0], current_pair[1] + 1)):

                if value == 0:

                    top_neighbour = (current_pair[0], current_pair[1] + 1)

                    xDistance = self.shift_to_origin(self.goal_pair)[0] - top_neighbour[0]
                    yDistance = self.shift_to_origin(self.goal_pair)[1] - top_neighbour[1]
                    if xDistance < 0:
                        xDistance = xDistance*(-1)
                    if yDistance < 0:
                        yDistance = yDistance*(-1)
                    
                    heuristics = xDistance + yDistance

                    point = [self.shift_from_origin(top_neighbour), self.shift_from_origin(current_pair), count + 1, heuristics]
                    possiblePoints.append(point)

            elif (current_pair[0] + 1) == key[0] and current_pair[1] == key[1] and direction != "l" and self.check_for_block((current_pair[0] + 1, current_pair[1])):

                if value == 0:

                    right_neighbour = (current_pair[0] + 1, current_pair[1])

                    xDistance = self.shift_to_origin(self.goal_pair)[0] - right_neighbour[0]
                    yDistance = self.shift_to_origin(self.goal_pair)[1] - right_neighbour[1]

                    if xDistance < 0:
                        xDistance = xDistance*(-1)
                    if yDistance < 0:
                        yDistance = yDistance*(-1)
                    
                    heuristics = xDistance + yDistance

                    point = [self.shift_from_origin(right_neighbour), self.shift_from_origin(current_pair), count + 1, heuristics]
                    possiblePoints.append(point)

            elif current_pair[0] == key[0] and (current_pair[1] - 1) == key[1] and direction != "t" and self.check_for_block((current_pair[0], current_pair[1] - 1)):

                if value == 0:

                    bottom_neighbour = (current_pair[0], current_pair[1] - 1)

                    xDistance = self.shift_to_origin(self.goal_pair)[0] - bottom_neighbour[0]
                    yDistance = self.shift_to_origin(self.goal_pair)[1] - bottom_neighbour[1]

                    if xDistance < 0:
                        xDistance = xDistance*(-1)
                    if yDistance < 0:
                        yDistance = yDistance*(-1)
                    
                    heuristics = xDistance + yDistance

                    point = [self.shift_from_origin(bottom_neighbour), self.shift_from_origin(current_pair), count + 1, heuristics]
                    possiblePoints.append(point)

            elif (current_pair[0] - 1) == key[0] and current_pair[1] == key[1] and direction != "r" and self.check_for_block((current_pair[0] - 1, current_pair[1])):

                if value == 0:

                    left_neighbour = (current_pair[0] - 1, current_pair[1])

                    xDistance = self.shift_to_origin(self.goal_pair)[0] - left_neighbour[0]
                    yDistance = self.shift_to_origin(self.goal_pair)[1] - left_neighbour[1]

                    if xDistance < 0:
                        xDistance = xDistance*(-1)
                    if yDistance < 0:
                        yDistance = yDistance*(-1)
                    
                    heuristics = xDistance + yDistance

                    point = [self.shift_from_origin(left_neighbour), self.shift_from_origin(current_pair), count + 1, heuristics]
                    possiblePoints.append(point)

        return possiblePoints


    def goal_reached(self, open_nodes):

        for node in open_nodes:

            if node[0] == self.goal_pair:

                # print("GOAL STATE REACHED")

                return True
        
        return False


    def checkClosedNode(self, lowest_node, closed_nodes):

        for node in closed_nodes:

            if node[0] == lowest_node[0] and node[1] == lowest_node[1]:
                return True

        return False


    def findLowestNode(self, equal_distance_nodes, closed_nodes):

        lowest_node = []

        if len(equal_distance_nodes) > 1:

            low_heuristics = equal_distance_nodes[0][3]
            lowest_node = equal_distance_nodes[0]

            for node in equal_distance_nodes:

                if not(self.checkClosedNode(node, closed_nodes)):

                    if node[3] < low_heuristics:

                        lowest_node = node
                        low_heuristics = node[3]
                    
                    elif node[3] == low_heuristics:

                        node_direction = self.find_direction(node)
                        lowest_node_direction = self.find_direction(lowest_node)

                        if node_direction == "t":
                            lowest_node = node
                        elif lowest_node_direction == "t":
                            lowest_node = lowest_node
                        elif node_direction == "r":
                            lowest_node = node
                        elif lowest_node_direction == "r":
                            lowest_node = lowest_node
                        elif node_direction == "b":
                            lowest_node = node
                        elif lowest_node_direction == "b":
                            lowest_node = lowest_node
                        elif node_direction == "l":
                            lowest_node = node
                        else:
                            lowest_node = lowest_node

        else:

            lowest_node = equal_distance_nodes[0]

        return lowest_node


    def retrace_path(self, closed_nodes):

        path = []

        prev_node = self.goal_pair

        while prev_node != self.initial_pair:
            for node in closed_nodes:
                if node[0] == prev_node:
                    prev_node = node[1]
                    path.append(node)
        
        return path[::-1]
    
    
    def AStarPathPlanning(self):

        open_nodes = self.find_neighbours(self.initial_pair, 0, self.initial_pair)

        closed_nodes = []

        while not(self.goal_reached(open_nodes)):

            if len(open_nodes) > 1:

                lowest_node = open_nodes[0]
                lowest_distance = lowest_node[2] + lowest_node[3]

            elif len(open_nodes) == 1:

                lowest_node = open_nodes
                lowest_distance = lowest_node[2] + lowest_node[3]

            for node in open_nodes:
                
                if node[2] + node[3] < lowest_distance:

                    lowest_distance = node[2] + node[3]

                elif node[2] + node[3] == lowest_distance:

                    if node[3] < lowest_node[3]:

                        lowest_distance = node[2] + node[3]

            equal_distance_nodes = []

            for node in open_nodes:

                if node[2] + node[3] == lowest_distance:

                    equal_distance_nodes.append(node)

            lowest_node = self.findLowestNode(equal_distance_nodes, closed_nodes)
            
            open_nodes.remove(lowest_node)
            closed_nodes.append(lowest_node)

            direction = self.find_direction(lowest_node)

            # print(lowest_node, "", direction)

            new_nodes = self.find_neighbours(lowest_node[0], lowest_node[2], lowest_node[1])

            if len(new_nodes) != 0:

                remove_open_node = []
                remove_new_node = []

                for nodeO in open_nodes:
                    for nodeN in new_nodes:
                        if nodeN[0][0] == nodeO[0][0] and nodeN[0][1] == nodeO[0][1]:
                            if nodeO[2] + nodeO[3] >= nodeN[2] + nodeN[3]:
                                remove_open_node.append(nodeO)
                            else:
                                remove_new_node.append(nodeN)

                if len(remove_open_node) > 0:
                    for node in remove_open_node:
                        open_nodes.remove(node)
                
                if len(remove_new_node) > 0:
                    for node in remove_new_node:
                        new_nodes.remove(node)

                for node in new_nodes:
                    open_nodes.append(node)
        
        for node in open_nodes:
            
            if node[0] == self.goal_pair:
                closed_nodes.append(node)

        path = self.retrace_path(closed_nodes)

        self.path = path


    def convert_path(self):

        direction = []

        # print(self.path)

        for node in self.path:

            xDiff = node[0][0] - node[1][0]
            yDiff = node[0][1] - node[1][1]

            if yDiff > 0:
                direction.append("t")
            elif xDiff > 0:
                direction.append("r")
            elif yDiff < 0:
                direction.append("b")
            elif xDiff < 0:
                direction.append("l")
            
        return direction


# obj = AStar((-5, 6), (-7.25, 4.75))

# obj.AStarPathPlanning()

# directions = obj.convert_path()

# print(directions)

# filewriter = open("sector3.txt", "a")

# for direction in directions:
#     filewriter.write(direction + "\n")

# filewriter.close()
