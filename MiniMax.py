# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 21:54:14 2022

@author: Yashu
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sum_ar=0
    for i in arr:
        sum_ar=sum_ar+i
        
    print(sum_ar-max(arr),sum_ar-min(arr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
