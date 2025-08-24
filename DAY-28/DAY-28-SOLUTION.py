import math
import os
import random
import re

if __name__ == '__main__':
    N = int(input().strip())
    gmail_users = []

    for _ in range(N):
        firstName, emailID = input().strip().split()
        # Regex to match Gmail addresses with letters, numbers, dot, underscore
        if re.match(r'^[\w\.]+@gmail\.com$', emailID):
            gmail_users.append(firstName)

    gmail_users.sort()

    for name in gmail_users:
        print(name)
