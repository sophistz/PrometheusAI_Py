import cv2
import numpy as np
import Map
import random
import math
import time

world = Map.initialize()
# cv2.imshow('Simulator', map)

x = 78
y = 78
theta = 78
v = 4


def doRandomMove(x, y, theta, v):
    front, frontLeft, frontRight, backLeft, backRight = getSignal(x, y, theta, v)
    # print(x, y, theta, front, frontLeft, frontRight, backLeft, backRight)

    map_copy = world.copy()
    cv2.rectangle(map_copy, (int(x - 3), int(y - 3)), (int(x + 3), int(y + 3)), (0, 0, 255), 2)
    cv2.line(map_copy, (int(x), int(y)), (int(x + frontLeft * math.cos(theta * math.pi / 180 + math.pi / 4)),
                                          int(y + frontLeft * math.sin(theta * math.pi / 180 + math.pi / 4))),
             (255, 0, 0), 1, 4)
    cv2.line(map_copy, (int(x), int(y)), (int(x + frontRight * math.cos(theta * math.pi / 180 - math.pi / 4)),
                                          int(y + frontRight * math.sin(theta * math.pi / 180 - math.pi / 4))),
             (255, 0, 0), 1, 4)
    cv2.line(map_copy, (int(x), int(y)), (int(x + backLeft * math.cos(theta * math.pi / 180 + 3 * math.pi / 4)),
                                          int(y + backLeft * math.sin(theta * math.pi / 180 + 3 * math.pi / 4))),
             (255, 0, 0), 1, 4)
    cv2.line(map_copy, (int(x), int(y)), (int(x + backRight * math.cos(theta * math.pi / 180 - 3 * math.pi / 4)),
                                          int(y + backRight * math.sin(theta * math.pi / 180 - 3 * math.pi / 4))),
             (255, 0, 0), 1, 4)
    cv2.line(map_copy, (int(x), int(y)),
             (int(x + front * math.cos(theta * math.pi / 180)), int(y + front * math.sin(theta * math.pi / 180))),
             (0, 255, 0), 1, 4)
    cv2.imshow('Simulator', map_copy)
    cv2.waitKey(1)

    # x, y, theta, v = getRandomMove(x, y, theta, v, action)


def getRandomMove(x, y, theta, v, action):
    theta_change = random.randint(-5 + 20 * action, 5 + 20 * action)
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
            theta += action * random.randint(10, 20)
            pass
    else:
        pass
    x = x + v * math.cos(theta * math.pi / 180)
    y = y + v * math.sin(theta * math.pi / 180)
    return (x, y, theta, v)


def crash(x, y, theta, v):
    if (x + v * math.cos(theta * math.pi / 180) < 5): return True
    if (x + v * math.cos(theta * math.pi / 180) > 495): return True
    if (y + v * math.sin(theta * math.pi / 180) < 5): return True
    if (y + v * math.sin(theta * math.pi / 180) > 495): return True
    if (x + v * math.cos(theta * math.pi / 180) > 95 and x + v * math.cos(
        theta * math.pi / 180) < 205 and y + v * math.sin(theta * math.pi / 180) > 95 and y + v * math.sin(
        theta * math.pi / 180) < 205): return True
    if (x + v * math.cos(theta * math.pi / 180) > 95 and x + v * math.cos(
        theta * math.pi / 180) < 205 and y + v * math.sin(theta * math.pi / 180) > 295 and y + v * math.sin(
        theta * math.pi / 180) < 405): return True
    if (x + v * math.cos(theta * math.pi / 180) > 295 and x + v * math.cos(
        theta * math.pi / 180) < 405 and y + v * math.sin(theta * math.pi / 180) > 95 and y + v * math.sin(
        theta * math.pi / 180) < 205): return True
    if (x + v * math.cos(theta * math.pi / 180) > 295 and x + v * math.cos(
        theta * math.pi / 180) < 405 and y + v * math.sin(theta * math.pi / 180) > 295 and y + v * math.sin(
        theta * math.pi / 180) < 405): return True
    return False


def getSignal(x, y, theta, v):
    global world
    front, frontLeft, frontRight, backLeft, backRight = (0, 0, 0, 0, 0)
    while (True):
        xx = int(x + front * math.cos(theta * math.pi / 180))
        yy = int(y + front * math.sin(theta * math.pi / 180))
        if (xx < 0 or xx > 499 or yy < 0 or yy > 499 or world[xx][yy][0] == 0):
            front -= 1
            break
        front += 1
    while (True):
        xx = int(x + frontLeft * math.cos(theta * math.pi / 180 + math.pi / 4))
        yy = int(y + frontLeft * math.sin(theta * math.pi / 180 + math.pi / 4))
        if (xx < 0 or xx > 499 or yy < 0 or yy > 499 or world[xx][yy][0] == 0):
            frontLeft -= 1
            break
        frontLeft += 1
    while (True):
        xx = int(x + frontRight * math.cos(theta * math.pi / 180 - math.pi / 4))
        yy = int(y + frontRight * math.sin(theta * math.pi / 180 - math.pi / 4))
        if (xx < 0 or xx > 499 or yy < 0 or yy > 499 or world[xx][yy][0] == 0):
            frontRight -= 1
            break
        frontRight += 1
    while (True):
        xx = int(x + backLeft * math.cos(theta * math.pi / 180 + 3 * math.pi / 4))
        yy = int(y + backLeft * math.sin(theta * math.pi / 180 + 3 * math.pi / 4))
        if (xx < 0 or xx > 499 or yy < 0 or yy > 499 or world[xx][yy][0] == 0):
            backLeft -= 1
            break
        backLeft += 1
    while (True):
        xx = int(x + backRight * math.cos(theta * math.pi / 180 - 3 * math.pi / 4))
        yy = int(y + backRight * math.sin(theta * math.pi / 180 - 3 * math.pi / 4))
        if (xx < 0 or xx > 499 or yy < 0 or yy > 499 or world[xx][yy][0] == 0):
            backRight -= 1
            break
        backRight += 1

    return (front, frontLeft, frontRight, backLeft, backRight)
    pass


def getReward(x, y, theta, v):
    # newX, newY, newTheta, newV = getRandomMove(x, y, theta, v)
    front, frontLeft, frontRight, backLeft, backRight = getSignal(x, y, theta, v)
    reward = calculateReward(front, frontLeft, frontRight, backLeft, backRight)
    return reward
    pass


def calculateReward(front, frontLeft, frontRight, backLeft, backRight):
    reward = 1 / (1 / front + 1 / frontLeft + 1 / frontRight + 1 / backLeft + 1 / backRight)
    return reward
    pass


q_table = np.zeros((11, 11, 11, 11, 11, 3))
epilon = 0.9
alpha = 0.1
gamma = 0.8


def signalTransfer(signal):
    a = signal // 10
    if a > 10: a = 10
    return a
    pass


def getQ(front, frontLeft, frontRight, backLeft, backRight):
    frontQ = signalTransfer(front)
    frontLeftQ = signalTransfer(frontLeft)
    frontRightQ = signalTransfer(frontRight)
    backLeftQ = signalTransfer(backLeft)
    backRightQ = signalTransfer(backRight)
    return (frontQ, frontLeftQ, frontRightQ, backLeftQ, backRightQ)
    pass


def checkAction(frontQ, frontLeftQ, frontRightQ, backLeftQ, backRightQ):
    global q_table
    return (q_table[frontQ][frontLeftQ][frontRightQ][backLeftQ][backRightQ] == 0).all()
    pass


def chooseAction(frontQ, frontLeftQ, frontRightQ, backLeftQ, backRightQ):
    global q_table
    a = q_table[frontQ][frontLeftQ][frontRightQ][backLeftQ][backRightQ][0]
    b = q_table[frontQ][frontLeftQ][frontRightQ][backLeftQ][backRightQ][1]
    c = q_table[frontQ][frontLeftQ][frontRightQ][backLeftQ][backRightQ][2]
    if (a > b and a > c):
        return -1
    elif (c > b):
        return 1
    else:
        return 0
    pass


def loadQTable():
    global q_table
    f = open("q_table.txt", "r")
    for a in range(11):
        for b in range(11):
            for c in range(11):
                for d in range(11):
                    for e in range(11):
                        aa = f.readline()
                        bb = np.array(list(map(float, aa.split(" "))))
                        q_table[a][b][c][d][e][0] = bb[0]
                        q_table[a][b][c][d][e][1] = bb[1]
                        q_table[a][b][c][d][e][2] = bb[2]
    f.close()
    pass


def saveQTable():
    global q_table
    f = open('q_table2.txt', 'w')
    for a in range(11):
        for b in range(11):
            for c in range(11):
                for d in range(11):
                    for e in range(11):
                        f.write(str(q_table[a][b][c][d][e][0]) + " " + str(q_table[a][b][c][d][e][1]) + " " + str(
                            q_table[a][b][c][d][e][0]) + "\n")
    f.close()
    pass


i = 0
j = 0
loadQTable()

while (True):

    # if i > 100000:
    #     saveQTable()
    #     break
    #     pass
    doRandomMove(x, y, theta, v)
    front, frontLeft, frontRight, backLeft, backRight = getSignal(x, y, theta, v)
    frontQ, frontLeftQ, frontRightQ, backLeftQ, backRightQ = getQ(front, frontLeft, frontRight, backLeft, backRight)

    if random.uniform(0, 1) > epilon or checkAction(frontQ, frontLeftQ, frontRightQ, backLeftQ, backRightQ):
        current_action = random.randint(-1, 1)
        i += 1
        pass
    else:
        current_action = chooseAction(frontQ, frontLeftQ, frontRightQ, backLeftQ, backRightQ)
        j += 1
        pass

    print(i, j)

    newX, newY, newTheta, newV = getRandomMove(x, y, theta, v, current_action)
    newFront, newFrontLeft, newFrontRight, newBackLeft, newBackRight = getSignal(newX, newY, newTheta, newV)
    newFrontQ, newFrontLeftQ, newFrontRightQ, newBackLeftQ, newBackRightQ = getQ(newFront, newFrontLeft, newFrontRight,
                                                                                 newBackLeft, newBackRight)
    best_new_action = chooseAction(newFrontQ, newFrontLeftQ, newFrontRightQ, newBackLeftQ, newBackRightQ)
    new_q = q_table[newFrontQ][newFrontLeftQ][newFrontRightQ][newBackLeftQ][newBackRightQ][best_new_action + 1]
    q_table[frontQ][frontLeftQ][frontRightQ][backLeftQ][backRightQ][current_action + 1] += alpha * (
                getReward(newX, newY, newTheta, newV) + gamma * new_q -
                q_table[frontQ][frontLeftQ][frontRightQ][backLeftQ][backRightQ][current_action + 1])
    x, y, theta, v = (newX, newY, newTheta, newV)
    pass

# cv2.destroyAllWindows()
