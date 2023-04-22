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


# Do some checking on user input looping until a postive int is entered.
# If the value is not a number then an exception is raised.
# If the number is negative, another pass of the loop is made.
# The loop can only be broken out of when a positive number is entered.
while True:   
    try:
        inputted_value = float(input("Please enter a positive number: "))
        if inputted_value > 0:
            break
        else:
            print("Not a positive number")
    except ValueError:
        print("Not a positive number")

# Call the function if the number is positive and digit
sq_root = sqrt(inputted_value)
# Print the answer to screen - rounded to 1 decimal place      
print(f"The square root of {inputted_value} is approx. {round(sq_root,1)}.")    
