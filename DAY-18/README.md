"""
# Day 18: Queues and Stacks

## Problem Statement
You are given a string `s`. Your task is to determine whether it is a palindrome by using:
- A stack (Last-In-First-Out)
- A queue (First-In-First-Out)

### Steps
1. Push and enqueue each character of the string into a stack and a queue respectively.
2. Compare the characters popped from the stack and dequeued from the queue.
3. If all characters match, the string is a palindrome.

---

## Input Format
A single string `s` containing only lowercase English letters.

---

## Output Format
If the string is a palindrome:
    The word, s, is a palindrome.
Otherwise:
    The word, s, is not a palindrome.

---

## Sample Input
racecar

## Sample Output
The word, racecar, is a palindrome.

---

## Explanation
- Stack (pop order): r → a → c → e → c → a → r
- Queue (dequeue order): r → a → c → e → c → a → r
Both match in reverse order, so the word is a palindrome.
"""

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
    
    def pushCharacter(self, ch):
        self.stack.append(ch)
    
    def enqueueCharacter(self, ch):
        self.queue.append(ch)
    
    def popCharacter(self):
        return self.stack.pop()
    
    def dequeueCharacter(self):
        return self.queue.pop(0)


# Read the string
s = input()
obj = Solution()

# Add all characters to stack and queue
for ch in s:
    obj.pushCharacter(ch)
    obj.enqueueCharacter(ch)

# Compare characters
isPalindrome = True
for i in range(len(s) // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

# Output result
if isPalindrome:
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")
