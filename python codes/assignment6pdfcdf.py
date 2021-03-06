# -*- coding: utf-8 -*-
"""assignment6pdfcdf.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19fN0_bp6A3xzPaM83vBNcKqOSF6XJ0sD
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import math
from scipy import stats
from scipy import integrate
import random

def pdf(x):
  if x >= 0 and x<=10:
    y=x/100
  elif x > 10 and x <= 20 :
    y=1/20 +0*x
  elif x >20 and x<=30 :
    y=(30-x)/200
  elif x>30:
    y=0
  return y
  
def cdf(x):
  if x >=0 and x<=10 :
    y=x**2/200
  elif x >10 and x<=20 :
    y=(x-5)/20
  elif x >20 and x<=30 :
    y=(60*x-500-x**2)/400
  elif x>30:
    y=1
  return y


print(f'theoretrical P(x+y>20)=',1-cdf(20))

vpdf=np.vectorize(pdf)
x1=np.linspace(0,40)
y1=vpdf(x)
plt.plot(x1,y1)
plt.xlabel("X+Y")
plt.ylabel("PDF")
plt.title("PDF of X+Y")
plt.grid()
plt.show()

vcdf=np.vectorize(cdf)
x2=np.linspace(0,40)
y2=vcdf(x)

plt.plot(x,y2)
plt.xlabel("X+Y")
plt.ylabel("CDF")
plt.title("CDF of X+Y")
plt.grid()
plt.show()