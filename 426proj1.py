import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style
import matplotlib as mpl
import random
import pylab
from random import gauss
from random import seed
import seaborn as sns
mpl.style.use('classic')

# written by Maria Galloway-Sprietsma
# PHYS 426 Programming Project, Spring 2021
# This code is a random walk calculation. It first creates random steps in 3D (x, y, z), sums them, squares them,
# and then runs through this 10,000 times to get a series of displacement vectors (R^2). These values are plotted
# in a histogram below. 
# To run code, use "python 426proj1.py" in a terminal with Python 3.7-3.8 installed 

def RandomWalk():
    N = 100 # number of steps
    def summation(): # this function sums the 3D vector for the histogram
        x = np.random.uniform(-1, 1, size=(N, 1))   # x direction
        xs = np.sum(x)                              # sum in x direction
        y = np.random.uniform(-1, 1, size=(N, 1))   # y direction
        ys = np.sum(y)                              # sum in y direction
        z = np.random.uniform(-1, 1, size=(N, 1))   # z direction
        zs = np.sum(z)                              # sum in z direction
        v = np.dstack([xs, ys, zs])                 # create a 3D vector with x, y, z values
        n = v / np.sqrt(np.sum(v**2))               # checking normalization
        #R = np.sum(v)
        #R = np.sqrt(np.sum(v**2))
        R = np.square(np.sqrt(np.sum(v**2))) # calculation of R^2   
        return R
    R_list = []
    for i in range(10000): # repeating the summation 10,000 times and appending that to a list
        R_list.append(summation())
    #R_avg = np.average((np.square(R_list)))
    R_avg = np.average(R_list) # this is the average value of R^2
    print("The average R^2 value is:", R_avg)
    #print(R2_list)

    fig, ax = plt.subplots()
    num_bins = 1000
    #n, bins, patches = plt.hist(R_list, num_bins, facecolor='red', alpha=0.5) # alternative histogram
    sns.distplot(R_list, bins=100, norm_hist=True, fit=None, kde=False, color='red') # histogram with normalized probability values
    ax.set(xlabel=r"R$^2$ (displacement squared)", ylabel='Probability', title="N=100")
    ax.set_xlim(left=-100)
    plt.show()
    #plt.savefig('2N1000.png', dpi=600) # saving figure
RandomWalk()

