T = int(input())  # Number of test cases

for _ in range(T):
    s = input()
    even = s[0::2]
    odd = s[1::2]
    print(even,odd,sep=" ")
