'''
es.py
Author: Eilis Donohue
Week 7 assignment
Read in a text file (using a command line argument)
Count the instances of a certain character in the file and output
Text file taken from: https://github.com/laumann/ds/tree/master/hashing/books
https://www.digitalocean.com/community/tutorials/python-command-line-arguments
'''


import sys
#FILENAME = "pride_and_prejudice.txt"
#FILENAME = "test.txt"
FILENAME = sys.argv[1]

search_char = "e"
char_count = 0

with open(FILENAME, 'r') as f:
    for line in f:
       char_count = line.count(search_char) + char_count

print(char_count)

