import tensorflow as tf
import numpy as np

f = open('data.txt', 'r')
a = []
for _ in range(1001):
    line = f.readline()
    a.append(list(map(float, line.split())))
    pass
data = np.array(a)
data = data[0:10, 1:]
data = data/100
print(data)
b = []
for i in range(10):
    b.append([(a[i+1][0]-a[i][0])])
label = np.array(b)/200
print(label)

x = tf.placeholder(tf.float32, [None, 5])
y = tf.placeholder(tf.float32, [None, 1])

w1 = tf.Variable(tf.random_normal([5, 10]))
b1 = tf.Variable(tf.zeros([10]))

l1 = tf.nn.tanh(tf.matmul(x, w1)+b1)

w2 = tf.Variable(tf.random_normal([10, 1]))
b2 = tf.Variable(tf.zeros([1]))

prediction = tf.nn.tanh(tf.matmul(l1, w2)+b2)

# prediction = tf.nn.tanh(tf.matmul(x, w1)+b1)

loss = tf.reduce_mean(tf.square(y-prediction))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(400000):
        sess.run(train_step, feed_dict={x: data[i%10:i%10+1], y: label[i%10:i%10+1]})
        print(sess.run(prediction, feed_dict={x: data[0:10]}))
        pass
    prediction_value = sess.run(prediction, feed_dict={x: data[0:10]})
    # ma1 = sess.run(w1)
    # # ma2 = sess.run(w2)
    # print(prediction_value)
    # print(ma1)
    # # print(ma2)
    # print(sess.run(loss, feed_dict={x: data[0:4], y: label[0:4]}))
    pass


f.close()