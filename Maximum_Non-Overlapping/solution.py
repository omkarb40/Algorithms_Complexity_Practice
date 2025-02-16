#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    tasks = []

    for _ in range(n):
        tasks.append(list(map(int, input().rstrip().split())))

    # Write your code here
    tasks.sort(key=lambda x: x[1])

    count = 0
    last_finish_time = -1

    for task in tasks:
        start, finish = task
        if start >= last_finish_time:
            count += 1
            last_finish_time = finish

    print(count)
