#!/usr/bin/python3
import tensorflow as tf
from os import environ
from sys import argv
environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
n = tf.Variable(3.0, tf.float32)
value = n*(n+1)/2
y = tf.placeholder(tf.float32)
loss = tf.square(value - y)
optimizer = tf.train.GradientDescentOptimizer(.01)
train = optimizer.minimize(loss)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000):
  sess.run(train, {y:float(argv[1])})
curr_n, curr_loss = sess.run([n,loss], {y:float(argv[1])})
print('n=',curr_n,', loss=',curr_loss)

