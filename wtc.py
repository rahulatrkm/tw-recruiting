#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'closest' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#
def binary_search(words, low, high, key):
    if high < low:
        return -1

    mid = (low + high) // 2 # the // operation does integer division

    if words[mid] < key:
        return binary_search(words, mid + 1, high, key) # check right of mid
    elif words[mid] > key:
        return binary_search(words, low, mid - 1, key) # check left of mid
    else:
        return mid # we found the word at mid

def closest(s, queries):
    # Write your code here
    sd = dict()
    for i,j in enumerate(s):
        if j in sd:
            sd[j].append(i)
        else:
            sd[j] = [i]
    a = []
    for query in queries:
        temp = sd[s[query]]
        if len(temp) == 1:
            a.append(-1)
        else:
            t1 = binary_search(temp, 0, (len(temp)-1), query)
            if t1 == 0:
                a.append(temp[1])
            elif t1 == (len(temp)-1):
                a.append(temp[t1-1])
            else:
                if abs(temp[t1-1] - query) <= abs(temp[t1+1] - query):
                    a.append(temp[t1-1])
                else:
                    a.append(temp[t1+1])

    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = closest(s, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
