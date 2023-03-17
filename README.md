
<h1><img align="right" height="150" src="img/ATU-Logo-Full-RGB-Green.jpg"> Assessments for Programming and Scripting 
</h1>
<p> 
Course: HDip in Computing in Data Analytics <br>
Module: Programming and Scripting <br>
Lecturer: Andrew Beatty
</p>

Student: Eilis Donohue (G00006088)

A repository for the solutions to the problem sheets given in the Programming Module of the HDip in Data Analytics 

Software Used: Python v3.7  [HOLD]


## Table of Contents:
1. [Task 1 (helloworld.py)](#task1)
2. [Task 2 (bank.py)](#task2)
3. [Task 3 (accounts.py)](#task3)
4. [Task 4 (collatz.py)](#task4)


## Task 1 (helloworld.py) <a id="task1"></a> 
Task Description:
<i> This file should contain a python program that displays Hello World! when it is run. </i>

Program Description:
 - Print statement to print **Hello World!**


## Task 2 (bank.py) <a id="task2"></a> 
Task Description:

<i> 
Prompt the user and read in two money amounts (in cent)
Add the two amounts
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. </i>

```
$ python bank.py
Enter amount1(in cent): 65
Enter amount2(in cent): 180
The sum of these is €2.45
```

Program Description:
 - The program asks user for 2 inputs in cents which are stored as ints.
 - Adds the 2 inputs 
 - Uses // 10 to floor the sum which gives the euro amount (this avoids a float being created).
 - Uses % 10 to get the cents remainder (again to avoid a float type being created).
 - Outputs a message to display the total.

Notes:
The user must enter an integer value. Any other input will cause a program error.

 References:
 1. String formatting: https://www.w3schools.com/python/python_string_formatting.asp
 2. [HOLD] reference to floor and remainder

## Task 3 (accounts.py) <a id="task3"></a> 
Task Description:

<i>Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).</i>

```
$ python accounts.py
Please enter an 10 digit account number: 1234567890
XXXXXX7890
```

Program Description:
  - The program prompts the user for a 10 digit account number.
  - The output is the last 4 digits of the number with the rest of the number padded with 'X' [1]. 
  

References:
1. Padding a string: https://www.w3schools.com/python/ref_string_rjust.asp


Notes:
If fewer than 10 digits are entered, the last 4 digits will still be revealed. 
    [HOLD] Future extras: Some checking on input being anything other than digits etc.

## Task 4 (collatz.py) <a id="task4"></a> 
Task Description:
<i> Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

Push the program in your pands-problem-sheet GitHub repository (like you do for all the weekly tasks).

Example of it running: </i> 
```
$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1
```
Program Description:

