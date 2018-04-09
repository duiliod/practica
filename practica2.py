#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 15:45:07 2018

@author: duilio
"""

from scipy import misc
f = misc.face()
misc.imsave('face.png', f) # uses the Image module (PIL)

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()


f = misc.face(gray=True)  # retrieve a grayscale image


plt.imshow(f, cmap=plt.cm.gray)   
plt.contour(f, [10, 20])    


#face = misc.face(gray=True)

lx, ly = face.shape

crop_face = face[lx // 4: - lx // 4, ly // 4: - ly // 4]
plt.imshow(crop_face)