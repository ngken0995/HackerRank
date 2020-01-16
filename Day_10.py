#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = bin(int(input()))
    n = n[2:]
    n = n.split('0')

    print(len(max(n)))
