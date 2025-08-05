import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = -63  # Minimum possible hourglass sum (-9 * 7)

    for i in range(4):  # 6 rows - 2
        for j in range(4):  # 6 cols - 2
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            hourglass_sum = top + middle + bottom
            max_sum = max(max_sum, hourglass_sum)

    print(max_sum)
