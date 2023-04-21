'''
collatz.py
Author: Eilis Donohue
week 4 assignment
Description: take a positive integer value
apply collatz conjecture to it, appending each value to a list
print the values of the list
***The program is fully commented and reproduced in  README.ipynb***
'''


# Do some checking on user input allowing for any input and looping until
# a postive int is entered. if the value is not an int then an exception is 
# thrown, if it's an int but negative, another pass of the loop is made.
# The loop can only be broken out of when a positive integer is entered.
while True:   
    try:
        user_inp = int(input("Please enter a positive integer: "))
        if user_inp > 0:
            break
        else:
            print("Not a positive integer value")
    except ValueError:
        print("Not a positive integer value")

# define variable user_list as the list for the calculated values
user_list = []   
    
#while user_inp <= 0:
#    user_inp = int(input("Please enter a positive integer: "))

# store the user input in the list
user_list.append(user_inp)

# execute collatz, appending values to the list until the value reaches 1 
while user_inp != 1:
    # checks if positive or negative
    if user_inp % 2 == 0:
        user_inp = int(user_inp // 2) # Using // to return an int
    else:
        user_inp = int((user_inp * 3) + 1)
    # appends the calculated value to the list    
    user_list.append(user_inp)

# print out the calculated values on the same line by looping over the values of user_list
for item in user_list:
    print(item, end=" ")

# goes to next line after printing the list of values
print()
