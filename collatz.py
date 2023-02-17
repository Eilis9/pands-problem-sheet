'''
collatz.py
Author: Eilis Donohue
week 4 assignment
take a positive integer value
apply collatz principle to it, appending each value to a list
print the values of the list
'''

# define variable user_list as the list for the calculated values
user_list = []

# initialise the user_inp so that it runs the loop to ask for user input
user_inp = -1

# execute this loop until the user inputs a positive int
while user_inp <= 0:
    user_inp = int(input("Please enter a positive integer: "))

# store the user input in the list
user_list.append(user_inp)

# execute collatz, appending values to the list until the value reaches 1 
while user_inp != 1:
    # checks if positive or negative
    if user_inp % 2 == 0:
        user_inp = int(user_inp / 2)
    else:
        user_inp = int((user_inp * 3) + 1)
    # appends the calculated value to the list    
    user_list.append(user_inp)

# print out the calculated values on the same line by looping over the values of user_list
for item in user_list:
    print(item, end=" ")

# goes to next line after printing the list of values
print()
