"""
plottask.py
Week 8 PANDS assignment
Author: Eilis Donohue
Description: A program which plots y=x^3 and a histogram with normal distribution
***The program is fully commented and reproduced in  README.ipynb***
"""


import numpy as np
import matplotlib.pyplot as plt
import math

#print(np.__version__)
rng = np.random.default_rng(1)

mean = 5
stdev = 2
pop_size = 1000
lower_range = 0
upper_range = 10

random_data = rng.normal(loc=mean, scale=stdev, size=pop_size)
x=np.arange(lower_range, upper_range+1)
y=x**3
print(random_data.min())
print(math.floor(random_data.min()))
print(math.ceil(random_data.min()))

bins = np.arange(-2, 12)


plt.hist(random_data, label="Normal Dist", bins=bins)
plt.plot(x, y, color='red', label='y=x^3')
plt.grid(linestyle='--', linewidth=1)
plt.title("Normal Distribution and function y=x^3")
plt.legend()
#plt.show()

#https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random
#rng = rng.standard_normal(loc=5, scale=2, size=100)

#random_data = rng.normal(loc=5, scale=2, size=100)