import math
import os
import random
import re
import sys

meal_cost = float(input())

tip_percent = int(input())

tax_percent = int(input())

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):


    tip = meal_cost*(tip_percent/100.0)

    tax = meal_cost*(tax_percent/100.0)

    return round(meal_cost+tip+tax)



print(solve(meal_cost, tip_percent, tax_percent))
