import numpy as np

# filereader = open("grid_data.txt", "r")
# grid_dict = {}
# grids = filereader.read().split(", ")
# print(len(grids))
# filereader.close()

filereader = open("grid.txt", "r")
grid_dict = {}
grids = filereader.read().split("\n")
filereader.close()

for grid in grids:
    if grid != "":
        string = grid.split(" ")
        grid_dict.update({(int(string[0]), int(string[1])) : int(string[2])})

# i = 0
# j = 0

# for grid in grids:
#     grid_dict.update({(i,j): int(grid)})
#     # print(grid)
#     j = j + 1
#     if j == 399:
#         j = 0
#         i = i + 1


# print(len(grid_dict))

# filewriter = open("grid_map.txt", "a")

# for key, value in grid_dict.items():
#     if key[1] == 601:
#         filewriter.write("\n")
#     elif key[0] == 300 and key[1] == 300:
#         filewriter.write("x")
#     else:
#         if value == 0:
#             filewriter.write(" ")
#         elif value == 1:
#             filewriter.write("|")
#         elif value == 2:
#             filewriter.write("0")

# filewriter.close()

# new_grid_dict = {}

# counti = 0
# countj = 0

# new_grid_dict.update()

grid_array = []

for key, value in grid_dict.items():
    grid_array.append(value)
    
data = np.array(grid_array).reshape(602,602)

data = np.transpose(data)

filewriter = open("grid_map.txt", "a")

# # for key, value in grid_dict.items():
# #     if key[1] == 601:
# #         filewriter.write("\n")
# #     elif key[0] == 300 and key[1] == 300:
# #         filewriter.write("x")
# #     else:
# #         if value == 0:
# #             filewriter.write(" ")
# #         elif value == 1:
# #             filewriter.write("|")

data = np.rot90(data)

i = 0
j = 0

while i != 602 and j != 602:
    
    if j == 601:
        filewriter.write("\n")
    elif i == 300 and j == 300:
        filewriter.write("x")
    elif data[i][j] == 0:
        filewriter.write(" ")
    elif data[i][j] == 1:
        filewriter.write("|")
    elif data[i][j] == 2:
        filewriter.write(" ")

    j = j + 1
    if j == 602:
        j = 0
        i = i + 1


filewriter.close()
