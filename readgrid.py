# filereader = open("grid.txt", "r")
# grid_Dict = {}
# grids = filereader.read().split("\n")
# filereader.close()

# for grid in grids:
#     if grid != "":
#         string = grid.split(" ")
#         grid_Dict.update({(int(string[0]), int(string[1])) : int(string[2])})

# for (i,j) in grid_Dict.items():
#     print("Key =", i, "Value =", j)


filereader = open("grid_data.txt", "r")
grid_dict = {}
grids = filereader.read()
print(len(grids))
filereader.close()