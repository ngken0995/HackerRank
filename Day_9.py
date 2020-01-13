#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def fact(n):
    if n <= 1:
        return 1;
    else  :  
        return n*fact(n-1);    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = fact(n)

    fptr.write(str(result) + '\n')

    fptr.close()
