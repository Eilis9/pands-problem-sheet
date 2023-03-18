"""
squareroot.py
Week 6 PANDS assignment
Author: Eilis Donohue
Description: A function which calculates the root of an inputted number
using Newton's method 
***The program is fully commented and reproduced in  README.ipynb***
"""


def sqrt(a, tolerance=0.0001):
    # Set the tolerance_check value
    tolerance_check = tolerance + 1   
    # Define an initial guess value            
    x0 = a / 2
    while abs(tolerance_check) > tolerance:      
        # Newton's method   
        x1 = 0.5 * (x0 + (a / x0))          
        # convergence check
        tolerance_check = (x1 - x0) / x0
        x0 = x1
    return x1


# Take in the value to be calculated
inputted_value = float(input("Please enter a positive number: "))
# Call the function
sq_root = sqrt(inputted_value)
# Print the answer to screen - rounded to 1 decimal place      
print(f"The square root of {inputted_value} is approx. {round(sq_root,1)}.")    


