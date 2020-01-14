# import sys
#
# data = []
# for line in sys.stdin:
#     data.append(line)
#
# if len(data) > 0:
#     sys.stdout.write(data + "\n")


#!/bin/python

import os
import random
import re
import sys


# Complete the findNumber function below.
# Complete the oddNumbers function below.
def oddNumbers(l, r):
    result = [x for x in range(l, r+1) if x%2 !=0]
    return result