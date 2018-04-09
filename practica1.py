# -*- coding: utf-8 -*-
"""
Editor de Spyder
    
Este es un archivo temporal
"""


#
import numpy as np
import matplotlib.pyplot as plt

#img=plt.imread ('likegeeks.png')

from scipy import misc

#face = misc.face()
#
#misc.imsave('face.png', face) # First we need to create the PNG file

face = misc.imread('likegeeks.png')
plt.imshow(face)
#import tensorflow as tf
#arr = np.array([1, 5.5, 3, 15, 20])
#tensor = tf.convert_to_tensor(arr,tf.float64)
#sess = tf.Session()
#print(sess.run(tensor))
#print(sess.run(tensor[1]))
#
#import input_data
#mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
#x = tf.placeholder("float", [None, 784])
#
#W = tf.Variable(tf.zeros([784,10]))
#
#b = tf.Variable(tf.zeros([10]))
#
#y = tf.nn.softmax(tf.matmul(x,W) + b)
#
#y_ = tf.placeholder("float", [None,10])




