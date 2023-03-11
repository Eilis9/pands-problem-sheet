"""
Week 6 assignment
squareroot.py
A function which calculates the root of an inputted number
Uses Newton-Raphson method: 
https://en.wikipedia.org/wiki/Newton%27s_method
Author: Eilis Donohue
"""


def sqrt(inputted_value, tolerance=0.0001):
    # The tolerance check value which will be used
    # to calculate the solution convergence needs to be initialised so it can 
    # be used in the loop to check against the required tolerance
    tolerance_check = tolerance + 1   
    # Define an initial guess value            
    x0 = inputted_value / 2
    while abs(tolerance_check) > tolerance:      
        # Function f is solved for 0 (root)
        f = x0 ** 2
        # f_dash is derivative of f
        f_dash = 2 * x0
        # Newton-Raphson method implementation
        x1 = x0 - ((f - inputted_value) / f_dash)
        # Calculate the convergence / error
        tolerance_check = (x1 - x0) / x0
        x0 = x1
    return x1


# Take in the value to be calculated
inputted_value = float(input("Please enter a positive number: "))
sq_root = sqrt(inputted_value)
# Print the answer to screen - rounded to 1 decimal place      
print(f"The square root of {inputted_value} is approx. {round(sq_root,1)}.")    


