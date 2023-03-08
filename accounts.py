'''accounts.py
Week 3 PANDS task assignment 
Author: Eilis Donohue
Asks for a 10 char input and outputs only the last 4 digits
'''

# Ask the user for 10 digit number
user_input = input("Please enter a 10 digit account number: ")

# strip any whitespace from start and finish - maybe remove later 
input_stripped = user_input.strip()

# find the length of the input string (no spaces)
input_string_length = len(input_stripped)

# check if all the characters are digits  - not used right now
all_digits_chk = input_stripped.isdigit()

# Using a slice for now to get the last 4 chars of the input string
output_string = input_stripped[-4:]

# pad the output with Xs depending on the length of the user input  
# - inputs less than 4 digits will output just that input
output_string_any = input_stripped[-4:].rjust(input_string_length, 'X')

# Print statement for account numbers of any length 
print(output_string_any)