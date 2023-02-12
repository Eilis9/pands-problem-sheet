# accounts.py
# Author: Eilis Donohue
# Week 3 task - asks for a 10 char input and outputs only the last 4 digits


# Ask the user for 10 digit number
user_input = input("Please enter a 10 digit account number: ")

# user_input = " 0001234567890"
# strip any whitespace from start and finish - maybe remove later (perhaps add an error check instead).
input_stripped = user_input.strip()

# find the length of the input string (no spaces)
input_string_length = len(input_stripped)

# check if all the characters are digits  - not used right now
all_digits_chk = input_stripped.isdigit()

#print("digit check is", all_digits_chk)

# Using a slice for now to get the last 4 chars of the input string
output_string = input_stripped[-4:]

# pad the output with Xs depending on the length of the user input  - inputs less than 4 digits will output just that input
output_string_any = input_stripped[-4:].rjust(input_string_length, 'X')

# print the account number with 6 Xs and just the last 4 digits inputted. This assumes a 10 digit input (ignoring trailing whitespaces)
print("XXXXXX" + output_string)

# print statement for account numbers of any length (inputs more than 4 digits will have leading digits padded with Xs)
print(output_string_any)