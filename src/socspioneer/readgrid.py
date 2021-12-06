filereader = open("grid.txt", "r")
grid = filereader.read().split("\n")
print(grid)
# string = ""
# while grid != "\n":
#     string = string + grid
#     grid = filereader.read(1)
 
# print(string)
filereader.close()