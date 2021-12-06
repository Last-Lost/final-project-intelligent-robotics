import math


def shift_to_origin(pair):
    X = -pair[1]*20 + 300
    Y = pair[0]*20 + 300
    Pair = (X, Y)
    return Pair

def shift_from_origin(pair):
    X = -(300 - pair[1])/20
    Y = -(pair[0] - 300)/20
    Pair = (X, Y)
    return Pair

shifted0 = shift_to_origin((2, 2))
shifted1 = shift_to_origin((2.05,2))
shifted2 = shift_to_origin((2, 2.05))
shifted3 = shift_to_origin((2, 1.95))
shifted4 = shift_to_origin((1.95,2))
# shifted5 = shiftorigin((4,9))
# shifted6 = shiftorigin((-4,9))
# shifted7 = shiftorigin((-4,-9))
# shifted8 = shiftorigin((4,-9))
print("x = " + str(shifted0[0]) + " y = " + str(shifted0[1]))
print("x = " + str(shifted1[0]) + " y = " + str(shifted1[1]))
print("x = " + str(shifted2[0]) + " y = " + str(shifted2[1]))
print("x = " + str(shifted3[0]) + " y = " + str(shifted3[1]))
print("x = " + str(shifted4[0]) + " y = " + str(shifted4[1]))
# print("x = " + str(shifted5[0]) + " y = " + str(shifted5[1]))
# print("x = " + str(shifted6[0]) + " y = " + str(shifted6[1]))
# print("x = " + str(shifted7[0]) + " y = " + str(shifted7[1]))
# print("x = " + str(shifted8[0]) + " y = " + str(shifted8[1]))


shifted5 = shift_from_origin(shifted0)
shifted6 = shift_from_origin(shifted1)
shifted7 = shift_from_origin(shifted2)
shifted8 = shift_from_origin(shifted3)
shifted9 = shift_from_origin(shifted4)


print("x = " + str(shifted5[0]) + " y = " + str(shifted5[1]))
print("x = " + str(shifted6[0]) + " y = " + str(shifted6[1]))
print("x = " + str(shifted7[0]) + " y = " + str(shifted7[1]))
print("x = " + str(shifted8[0]) + " y = " + str(shifted8[1]))
print("x = " + str(shifted9[0]) + " y = " + str(shifted9[1]))

path = ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'r', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'r', 'b', 'r', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'r', 'b', 'r', 'r', 'b', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'r', 'b', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'b', 'r', 'b', 'b', 'r', 'r', 'b', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'r', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']

print(len(path))


filereader = open("sector3.txt", "r")
directions = filereader.read().split("\n")
filereader.close()

directions.remove("")

print(directions)

rotate = (3*math.pi/2)

# if rotate 
t = math.sin(rotate) == 1
r = math.cos(rotate) == 1
b = math.sin(rotate) == -1
l = math.cos(rotate) == -1

