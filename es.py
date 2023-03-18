'''
es.py
Week 7 PANDS assignment
Author: Eilis Donohue
Description: Read in a text file (using a command line argument)
Count the instances of a certain character in the file and output
Text file taken from:  https://github.com/laumann/ds/tree/master/hashing/books
https://www.digitalocean.com/community/tutorials/python-command-line-arguments
https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
ignore errors: https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
encoding : https://stackoverflow.com/questions/26324622/what-characters-do-not-directly-map-from-cp1252-to-utf-8
https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
***The program is fully commented and reproduced in  README.ipynb***
'''


import sys
#FILENAME = "pride_and_prejudice.txt"
#FILENAME = "war_and_peace.txt"
#FILENAME = "test.txt"
#  Take the filename from the command line
FILENAME = sys.argv[1]

search_char = "e"
char_count = 0

# Open the file and ignore any errors thrown by unknown characters
# Avoids issues when reading non utf-8 encoded files.
with open(FILENAME, 'rt', errors='ignore') as f:
# Reading the file line by line to avoid buffer issues with large files
    for line in f:
       # Convert the line to all lower case before counting 'e' so that the count isn't case-sensitive       
       char_count = line.lower().count(search_char) + char_count

# print the number of 'e's
print(char_count)

