from sklearn import tree
import numpy as np
import random

f = open('data_2.txt', 'r')
a = []
for _ in range(1800):
    line = f.readline()
    a.append(list(map(float, line.split())))
    pass
data = np.array(a)
# print(data)
x_data = data[0:1200, 1:6]
y_data = data[0:1200, 6]
x_test = data[1200:1800, 1:6]
y_test = data[1200:1800, 6]
model = tree.DecisionTreeClassifier(criterion='entropy')
model.fit(x_data, y_data)

c=0
cc=0
for i in x_test:
    predict = model.predict(i.reshape(1, -1))
    if predict==y_test[c]: cc+=1
    print(y_test[c], predict, (predict==y_test[c]))
    c += 1
print(cc/c )
f.close()