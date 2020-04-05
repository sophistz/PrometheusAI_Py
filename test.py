import numpy as np
f = open("q_table.txt", "r")

a = f.readline()
b = np.array(list(map(float, a.split(" "))))
print(b[1]+1)
f.close()
