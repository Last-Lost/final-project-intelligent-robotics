import numpy as np

filereader = open("grid.txt", "r")
grid_dict = {}
grids = filereader.read().split("\n")
# print(len(grids), "Hi", grids[-1], "Hi")
filereader.close()

for grid in grids:
    if grid != "":
        string = grid.split(" ")
        grid_dict.update({(int(string[0]), int(string[1])) : int(string[2])})

grid_array = []

for key, value in grid_dict.items():
    grid_array.append(value)

data = np.array(grid_array).reshape(602,602)


data = np.rot90(data)
data = np.transpose(data)

# data = np.rot90(data)

# data = np.rot90(data)

ch1 = "                                                                                                    ||||******************     ****************   |********************  ** *******************************************************************************************************************    ********* "
ch2 = "********************************************************************************************************************************************************************************************************************  ***********  *****|||         |||                                 |||                 x"
print(len(ch1))
print(len(ch2))




print(data[480][220])
print(data[120][220])
print(data[120][380])
print(data[480][380])

print("\n")

print(data[380][120])
print(data[220][120])
print(data[220][480])
print(data[380][480])