'''
accounts.py
Week 3 PANDS assignment 
Author: Eilis Donohue
Description: Asks for a 10 char input and outputs only the last 4 digits
***The program is fully commented and reproduced in  README.ipynb***
'''

user_input = input("Please enter a 10 digit account number: ")

# Strip any whitespace from start and finish
user_input = user_input.strip()
input_string_length = len(user_input)

# Get last 4 chars
end_chars = user_input[-4:]

# Right justify end_chars and pad with Xs using length of the user input  
# - inputs less than 4 digits will output just that input
output_string = end_chars.rjust(input_string_length, 'X')
print(output_string)