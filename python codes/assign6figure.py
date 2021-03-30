# -*- coding: utf-8 -*-
"""assign6figure.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LMWOQfqETFHVx5Kwt-zr7pdqBOwNXskc
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import math
from scipy import stats
from scipy import integrate
import random
import decimal
count=0

def line(x):
  y= 20-x
  return y

def line1(x):
  y=0-0*x
  return y
def line2(x):
  y=20-0*x
  return y
def line3(x):
  y=10-0*x
  return y

x1=np.arange(0,10,0.01)
x2=np.arange(10,20,0.01)
y_x=np.arange(0,20,0.01)
y1=line(x1)
y2=line(x2)
y3=line1(x1)
y4=line2(x1)
x_1=line1(y_x)
x_2=line3(y_x)
plt.plot(x1,y1,color='black')
plt.plot(x2,y2,color='black')
plt.plot(x1,y3,color='black')
plt.plot(x1,y4,color='black')
plt.plot(x_1,y_x,color='black')
plt.plot(x_2,y_x,color='black')
plt.fill_between(x1,y1,y4)
plt.annotate("(10,20)",(10,20))
plt.annotate("(10,10)",(10,10))
plt.annotate("(0,20)",(0,20))
plt.annotate("(10,0)",(10,0))
plt.annotate("(0,0)",(0,0))
plt.grid()
plt.show()