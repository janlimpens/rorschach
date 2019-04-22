#!/usr/bin/env python
 
import argparse
import os
import os.path
import random

class Rorschach:

    cols = 0
    rows = 0
    str_rep = ""
        
    def __init__(self, cols, rows, items):
        self.cols = cols
        self.rows = rows
        shuffled = random.sample(items, len(items))
        matrix = self._create_matrix(shuffled)
        self._set_str_representation(matrix)

    def __str__(self):
        return self.str_rep

    def _create_matrix(self, items):
        return list(zip(*[iter(items)]*self.cols))[0:self.rows]

    def _set_str_representation(self, matrix):
        for arr in matrix:
            self.str_rep += ", ".join(arr) + "\n"

cols = 3
rows = 1
file_name = 'items.txt'

parser = argparse.ArgumentParser(description='Given a list of words, it creates a table from it.')
parser.add_argument('columns', type=int, nargs='?',
                    help='number of columns', default=cols)
parser.add_argument('rows', type=int, nargs='?',
                    help='number of rows', default=rows)
parser.add_argument('filename', nargs='?',
                    help='filename of word list', default=file_name)
args = parser.parse_args()

cols = args.columns
rows = args.rows
file_name = args.filename

path = os.path.join(os.getcwd(), file_name)

if not os.path.isfile(path):
    file = open(path, "w+") 
    file.write("write list of expressions here\nseparate them by line breaks\nall is well") 
    file.close()
else:
    file = open(path, "r")
    items = file.read().split('\n')
    file.close()
    print 'Using {0} as word list.\n'.format(path)
    print(Rorschach(cols, rows, items))
