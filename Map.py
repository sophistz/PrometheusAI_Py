import numpy as np

def initialize():

    map = np.empty((500, 500, 3))
    map[:, :, :] = 255

    map[100:200, 100:200, :] = 0
    map[100:200, 300:400, :] = 0
    map[300:400, 100:200, :] = 0
    map[300:400, 300:400, :] = 0

    return map