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
# See ref [x] - for setting the ticks on the x and y axis
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

# Set a range object to be a seeded random generator (for repeatability)
rng = np.random.default_rng(3)

# Set the parameters for the normal dist data generation
mean = 5
stdev = 2
pop_size = 1000
# Set the parameters for the function definition 
# assuming here that up to and including x=10 is required to be plotted
x_lower_range = 0
x_upper_range = 10
# Pick a major and minor axis ticks to suit the data
y_major_tick = 50
y_minor_tick = 10
x_major_tick = 1
x_minor_tick = 0.5
bin_size = 0.5

# Generate a numpy array or normally distributed data 
random_data = rng.normal(loc=mean, scale=stdev, size=pop_size)
# Find the lower and upper bounds of the random data to set the bins for 
# the histogram applying .floor and .ceil to the min and max of the data.
random_data_floor = math.floor(random_data.min())
random_data_ceiling = math.ceil(random_data.max())
# Define the array of bins using the min and max data - 
# Add 1 bin_size to he upper to capture the upper bound of the data
bins = np.arange(random_data_floor, random_data_ceiling+bin_size, bin_size)

# Define a numpy array with lower and upper bounds
# Assuming the brief is asking for data up to and including 10 so adding 1
# picking a step of 0.1 to get a good discretisation at low x values
x = np.arange(x_lower_range, x_upper_range + 1, 0.1)
# Define the function y as x cubed
y = x**3


# Return the fig and ax objects so that the axes ticks can be set[Ref X]
fig, ax = plt.subplots()

# Plot the histogram, setting the bins equal to the range created
# n is the tuple that is returned containing the values of the bins and bins themselves
n = plt.hist(random_data, label="Normal Dist", bins=bins)

# find the max value of the histogram bins
hist_max_y = n[0].max()

#Plot the function y=x^3
plt.plot(x, y, color='red', label='y=x^3')

# Set the maximum value of the y axis to suit the histogram data
# As the function data plotted is deterministic, there is no value in showing
# the function y=x^3 to its upper y-extent as the normal distributed data is not
# well displayed as a result.
plot_yaxis_max = (hist_max_y + y_major_tick) // y_major_tick
plot_yaxis_max = plot_yaxis_max * y_major_tick

# set the axis upper and lower bounds
plt.axis([random_data_floor, random_data_ceiling, 0, plot_yaxis_max])

# apply the x and y labels
plt.xlabel("X")
plt.ylabel("Frequency / y^3")
plt.grid(which='major', linestyle='-', linewidth=0.6)
plt.grid(which='minor', linestyle='-.', linewidth=0.4)
# Set the major and minor tick spacing [Ref X]
ax.xaxis.set_major_locator(MultipleLocator(x_major_tick))
ax.xaxis.set_minor_locator(MultipleLocator(x_minor_tick))
ax.yaxis.set_major_locator(MultipleLocator(y_major_tick))
ax.yaxis.set_minor_locator(MultipleLocator(y_minor_tick))

# Format the length of the ticks 
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', length=4)

# Set the title of the plot
plt.title("Normal Distribution np.random.default_rng(3) / y=x^3")

# Display the legend
plt.legend()

# Show the plot
plt.show()
