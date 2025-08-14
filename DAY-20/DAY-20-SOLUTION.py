import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    number_of_swaps = 0

# Bubble sort
for i in range(n):
    # Track if any swap is done in this pass
    swaps_in_this_pass = 0
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            number_of_swaps += 1
            swaps_in_this_pass += 1
    if swaps_in_this_pass == 0:
        break

print(f"Array is sorted in {number_of_swaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")

  
