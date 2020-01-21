import cv2
import numpy as np
import Map
import random
import math
import time

map = Map.initialize()
cv2.imshow('Simulator', map)

x = 78
y = 78
theta = 78
v = 5

def randomMove():
    global x, y, theta, v
    frontLeft, frontRight, backLeft, backRight = getSignal()
    print(x, y, theta, frontLeft, frontRight, backLeft, backRight)
    map_copy = map.copy()
    cv2.rectangle(map_copy, (int(x-3), int(y-3)), (int(x+3), int(y+3)), (0, 0, 255), 2)
    cv2.line(map_copy, (int(x), int(y)), (int(x+frontLeft*math.cos(theta*math.pi/180+math.pi/4)), int(y+frontLeft*math.sin(theta*math.pi/180+math.pi/4))), (255, 0, 0), 1, 4)
    cv2.line(map_copy, (int(x), int(y)), (int(x+frontRight*math.cos(theta*math.pi/180-math.pi/4)), int(y+frontRight*math.sin(theta*math.pi/180-math.pi/4))), (255, 0, 0), 1, 4)
    cv2.line(map_copy, (int(x), int(y)), (int(x+backLeft*math.cos(theta*math.pi/180+3*math.pi/4)), int(y+backLeft*math.sin(theta*math.pi/180+3*math.pi/4))), (255, 0, 0), 1, 4)
    cv2.line(map_copy, (int(x), int(y)), (int(x+backRight*math.cos(theta*math.pi/180-3*math.pi/4)), int(y+backRight*math.sin(theta*math.pi/180-3*math.pi/4)) ), (255, 0, 0), 1, 4)
    cv2.imshow('Simulator', map_copy)
    theta = theta + random.randint(-10, 10)
    while (crash()):
        theta = theta + random.randint(-10, 10)
    x = x+v*math.cos(theta*math.pi/180)
    y = y+v*math.sin(theta*math.pi/180)

def crash():
    global x, y, theta, v
    if (x + v * math.cos(theta*math.pi/180) < 0): return True
    if (x + v * math.cos(theta*math.pi/180) > 500): return True
    if (y + v * math.sin(theta*math.pi/180) < 0): return True
    if (y + v * math.sin(theta*math.pi/180) > 500): return True
    if (x + v * math.cos(theta*math.pi/180) > 95 and x + v * math.cos(theta*math.pi/180) < 205 and y + v * math.sin(theta*math.pi/180) > 95 and y + v * math.sin(theta*math.pi/180) < 205): return True
    if (x + v * math.cos(theta*math.pi/180) > 95 and x + v * math.cos(theta*math.pi/180) < 205 and y + v * math.sin(theta*math.pi/180) > 295 and y + v * math.sin(theta*math.pi/180) < 405): return True
    if (x + v * math.cos(theta*math.pi/180) > 295 and x + v * math.cos(theta*math.pi/180) < 405 and y + v * math.sin(theta*math.pi/180) > 95 and y + v * math.sin(theta*math.pi/180) < 205): return True
    if (x + v * math.cos(theta*math.pi/180) > 295 and x + v * math.cos(theta*math.pi/180) < 405 and y + v * math.sin(theta*math.pi/180) > 295 and y + v * math.sin(theta*math.pi/180) < 405): return True
    return False

def getSignal():
    global map, x, y, theta, v
    frontLeft, frontRight, backLeft, backRight = (0, 0, 0, 0)
    while (True):
        xx = int(x+frontLeft*math.cos(theta*math.pi/180+math.pi/4))
        yy = int(y+frontLeft*math.sin(theta*math.pi/180+math.pi/4))
        if (xx < 0 or xx > 499 or yy < 0 or yy > 499 or map[xx][yy][0] == 0):
            frontLeft -= 1
            print(xx, yy)
            break
        frontLeft += 1
    while (True):
        xx = int(x+frontRight*math.cos(theta*math.pi/180-math.pi/4))
        yy = int(y+frontRight*math.sin(theta*math.pi/180-math.pi/4))
        if (xx < 0 or xx > 499 or yy < 0 or yy > 499 or map[xx][yy][0] == 0):
            frontRight -= 1
            break
        frontRight += 1
    while (True):
        xx = int(x+backLeft*math.cos(theta*math.pi/180+3*math.pi/4))
        yy = int(y+backLeft*math.sin(theta*math.pi/180+3*math.pi/4))
        if (xx < 0 or xx > 499 or yy < 0 or yy >499 or map[xx][yy][0] == 0):
            backLeft -= 1
            break
        backLeft += 1
    while (True):
        xx = int(x+backRight*math.cos(theta*math.pi/180-3*math.pi/4))
        yy = int(y+backRight*math.sin(theta*math.pi/180-3*math.pi/4))
        if (xx < 0 or xx > 499 or yy < 0 or yy > 499 or map[xx][yy][0] == 0):
            backRight -= 1
            break
        backRight += 1

    return (frontLeft, frontRight, backLeft, backRight)
    pass

while (True):
    randomMove()
    cv2.waitKey(0)
    # k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    #
    # if k == 27:
    #     break
    # time.sleep(0.01)


cv2.waitKey(0)
cv2.destroyAllWindows()