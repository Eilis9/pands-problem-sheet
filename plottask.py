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
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

# Set a range object to be a seeded random generator (for repeatability)
rng = np.random.default_rng(1)

# Set the parameters for the data generation
mean = 5
stdev = 2
pop_size = 1000
lower_range = 0
upper_range = 10

# Generate a numpy array or normally distributed data 
random_data = rng.normal(loc=mean, scale=stdev, size=pop_size)
# Define a numpy array with lower and upper bounds
# Assuming the brief is asking for data up to and including 10
x=np.arange(lower_range, upper_range+1)
# Define the function y as x cubed
y=x**3
print(random_data.min())
# Find the lower and upper bounds of the random data to set the bins for 
# the histogram
random_data_floor = math.floor(random_data.min())
random_data_ceiling = math.ceil(random_data.max())
print(random_data.min(), math.floor(random_data.min()))
print(random_data.max(), math.ceil(random_data.max()))

# Define the array of bins using the min and max data - (add 1 to capture the upper bound of the data)
# Bin width is 0.5
bins = np.arange(random_data_floor, random_data_ceiling+1, 0.5)

# Return the fig and ax objects so that the axes ticks can be set[Ref X]
fig, ax = plt.subplots()
# Plot the histogram, setting the bins equal to the range created
plt.hist(random_data, label="Normal Dist", bins=bins)
#Plot the function 
plt.plot(x, y, color='red', label='y=x^3')
#
plt.xlabel("Random data or x")
plt.ylabel("Distribution or y^3")
plt.grid(which='major', linestyle='--', linewidth=0.6)
plt.grid(which='minor', linestyle='-.', linewidth=0.3)
# Set the major and minor tick spacing [Ref X]
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_major_locator(MultipleLocator(100))
ax.yaxis.set_minor_locator(MultipleLocator(20))
# Format the length of the ticks 
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', length=4)

#plt.grid(linestyle='--', linewidth=0.5)
# set the title of the plot
plt.title("Normal Distribution and function y=x^3")
# Display the legend
plt.legend()
# Show the plot
plt.show()
