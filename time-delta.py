#!/bin/python

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        t1 = raw_input()

        t2 = raw_input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
