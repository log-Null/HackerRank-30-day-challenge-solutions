import sys

n = int(input())
phone_book = {}

# Read the phone book entries
for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

# Read queries from remaining lines using stdin (ignores first n+1 lines)
for line in sys.stdin:
    query = line.strip()
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")
