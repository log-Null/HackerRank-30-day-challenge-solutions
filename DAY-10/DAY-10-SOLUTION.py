import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary = bin(n)[2:]        # Convert to binary and remove '0b'
    max_ones = max(len(s) for s in binary.split('0'))  # Count max streak of 1s
    print(max_ones)

