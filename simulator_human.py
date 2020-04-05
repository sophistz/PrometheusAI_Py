import cv2
import numpy as np
import Map
import random
import math
import time

world = Map.initialize()
cv2.imshow('Simulator', world)

x = 78
y = 78
theta = 78
v = 4

def doRandomMove(action):
    global x, y, theta, v
    front, frontLeft, frontRight, backLeft, backRight = getSignal(x, y, theta, v)
    # print(x, y, theta, front, frontLeft, frontRight, backLeft, backRight)

    map_copy = world.copy()
    cv2.rectangle(map_copy, (int(x-3), int(y-3)), (int(x+3), int(y+3)), (0, 0, 255), 2)
    cv2.line(map_copy, (int(x), int(y)), (int(x+frontLeft*math.cos(theta*math.pi/180+math.pi/4)), int(y+frontLeft*math.sin(theta*math.pi/180+math.pi/4))), (255, 0, 0), 1, 4)
    cv2.line(map_copy, (int(x), int(y)), (int(x+frontRight*math.cos(theta*math.pi/180-math.pi/4)), int(y+frontRight*math.sin(theta*math.pi/180-math.pi/4))), (255, 0, 0), 1, 4)
    cv2.line(map_copy, (int(x), int(y)), (int(x+backLeft*math.cos(theta*math.pi/180+3*math.pi/4)), int(y+backLeft*math.sin(theta*math.pi/180+3*math.pi/4))), (255, 0, 0), 1, 4)
    cv2.line(map_copy, (int(x), int(y)), (int(x+backRight*math.cos(theta*math.pi/180-3*math.pi/4)), int(y+backRight*math.sin(theta*math.pi/180-3*math.pi/4)) ), (255, 0, 0), 1, 4)
    cv2.line(map_copy, (int(x), int(y)), (int(x+front*math.cos(theta*math.pi/180)), int(y+front*math.sin(theta*math.pi/180))), (0, 255, 0), 1, 4)
    cv2.imshow('Simulator', map_copy)

    x, y, theta, v = getRandomMove(x, y, theta, v, action)

def getRandomMove(x, y, theta, v, action):
    theta_change = random.randint(-5+20*action, 5+20*action)
    theta += theta_change
    if (crash(x, y, theta, v)):
        theta -= theta_change
        # if (getSignal(x, y, theta, v)[1] < getSignal(x, y, theta, v)[2]):
        #     while (crash(x, y, theta, v)):
        #         theta -= random.randint(1, 10)
        # else:
        #     while (crash(x, y, theta, v)):
        #         theta += random.randint(1, 10)
        if (action == 0): action = 1
        while (crash(x, y, theta, v)):
            theta += action*random.randint(10, 20)
            pass
    else:
        pass
    x = x + v * math.cos(theta * math.pi / 180)
    y = y + v * math.sin(theta * math.pi / 180)
    return (x, y, theta, v)

def crash(x, y, theta, v):
    if (x + v * math.cos(theta*math.pi/180) < 5): return True
    if (x + v * math.cos(theta*math.pi/180) > 495): return True
    if (y + v * math.sin(theta*math.pi/180) < 5): return True
    if (y + v * math.sin(theta*math.pi/180) > 495): return True
    if (x + v * math.cos(theta*math.pi/180) > 95 and x + v * math.cos(theta*math.pi/180) < 205 and y + v * math.sin(theta*math.pi/180) > 95 and y + v * math.sin(theta*math.pi/180) < 205): return True
    if (x + v * math.cos(theta*math.pi/180) > 95 and x + v * math.cos(theta*math.pi/180) < 205 and y + v * math.sin(theta*math.pi/180) > 295 and y + v * math.sin(theta*math.pi/180) < 405): return True
    if (x + v * math.cos(theta*math.pi/180) > 295 and x + v * math.cos(theta*math.pi/180) < 405 and y + v * math.sin(theta*math.pi/180) > 95 and y + v * math.sin(theta*math.pi/180) < 205): return True
    if (x + v * math.cos(theta*math.pi/180) > 295 and x + v * math.cos(theta*math.pi/180) < 405 and y + v * math.sin(theta*math.pi/180) > 295 and y + v * math.sin(theta*math.pi/180) < 405): return True
    return False

def getSignal(x, y, theta, v ):
    global world
    front, frontLeft, frontRight, backLeft, backRight = (0, 0, 0, 0, 0)
    while (True):
        xx = int(x+front*math.cos(theta*math.pi/180))
        yy = int(y+front*math.sin(theta*math.pi/180))
        if (xx < 0 or xx > 499 or yy < 0 or yy > 499 or map[xx][yy][0] == 0):
            front -= 1
            break
        front += 1
    while (True):
        xx = int(x+frontLeft*math.cos(theta*math.pi/180+math.pi/4))
        yy = int(y+frontLeft*math.sin(theta*math.pi/180+math.pi/4))
        if (xx < 0 or xx > 499 or yy < 0 or yy > 499 or map[xx][yy][0] == 0):
            frontLeft -= 1
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

    return (front, frontLeft, frontRight, backLeft, backRight)
    pass

def getReward(x, y, theta, v, action=None):
    newX, newY, newTheta, newV = getRandomMove(x, y, theta, v)
    front, frontLeft, frontRight, backLeft, backRight = getSignal(newX, newY, newTheta, newV)
    reward = calculateReward(front, frontLeft, frontRight, backLeft, backRight, abs(newTheta-theta))
    pass

def calculateReward(front, frontLeft, frontRight, backLeft, backRight, thetaChange):
    reward = 1/(1/front+1/frontLeft+1/frontRight+1/backLeft+1/backRight)
    pass

while (True):
    doRandomMove(action)
    k = cv2.waitKey(100) & 0xff
    print(k)
    if k == 27:
        break
    elif k == 100:
        action = 1
    elif k == 97:
        action = -1
    else:
        action = 0


cv2.destroyAllWindows()