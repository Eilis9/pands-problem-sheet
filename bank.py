# bank.py
# Author: Eilis Donohue
# asks for 2 integer inputs, adds these and outputs the answer in euro

import math

# ask user for input
input1 = int(input("Enter amount1(in cent): "))
input2 = int(input("Enter amount2(in cent): "))

# add the inputs
totalCent = input1 + input2

# convert to euro
totalEuro = totalCent / 100

# print total formatted to 2 decimal places
print(f"The sum of these is €{totalEuro:.2f}")