'''
es.py
Week 7 PANDS assignment
Author: Eilis Donohue
Description: Read in a text file (using a command line argument)
Count the instances of a certain character in the file and output
***The program is fully commented and reproduced in  README.ipynb***
'''


import sys

#  Take the filename from the command line
FILENAME = sys.argv[1]

search_char = "e"
char_count = 0

# Open the file and ignore any errors thrown by unknown characters
with open(FILENAME, 'rt', errors='ignore') as f:
# Reading the file line by line to avoid errors with very large files
    for line in f:
       # Convert the line to all lower case before counting 'e' so that the count isn't case-sensitive       
       char_count = line.lower().count(search_char) + char_count

print(char_count)

