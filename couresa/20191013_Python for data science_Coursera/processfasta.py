#!/usr/bin/python3

'''
processfasta.py builds a dictionary with all sequences from a FASTA file
'''

import sys
filename = sys.argv[1]

try:
    f = open('filename')
except IOError:
    print('File %s does not exits!!' % filename)