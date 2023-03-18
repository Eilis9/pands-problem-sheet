'''
bank.py
Week 2 PANDS assignment 
Author: Eilis Donohue
Description: Prompts the user for 2 integer inputs 
Adds these and outputs the answer in euro and cent
***The program is fully commented and reproduced in  README.ipynb***
'''

# Prompt the user for input 
input1 = int(input("Enter amount1(in cent): "))
input2 = int(input("Enter amount2(in cent): "))

# Add the inputs
total_cent = input1 + input2

# Convert total to a string type so that string formatting can be applied
total_cent = str(total_cent)

# Last 2 digits of the string is the cent amount and everything else is euro.
# This avoids dividing and float types 

# Unless the total_cent amount is 10c or less when leading zeroes are
# required. 
leading_zeroes = "0" * (3 - len(total_cent))
total_cent = leading_zeroes + total_cent    

# String slices to get the euro amount and cent amount
euro_amount = total_cent[:-2]
cent_amount = total_cent[-2:]
  
# Output the amount 
print(f"The sum of these is €{euro_amount}.{cent_amount}")