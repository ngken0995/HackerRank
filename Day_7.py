import math
import os
import random
import re
import sys



if __name__ == '__main__':
    while True:
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        if n == len(arr):
            break
        else:
            continue

    rarr = map(str, arr[::-1])
    print(" ".join(rarr))
