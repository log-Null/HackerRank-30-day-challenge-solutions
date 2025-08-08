# Day 14: Scope – HackerRank 30 Days of Code Challenge

## 📌 Problem Statement
The challenge focuses on **object-oriented programming** and understanding **scope** in classes.  
We are given a `Difference` class that stores a list of integers. Our task is to:

1. Implement the constructor to store the array in a private variable.
2. Implement the `computeDifference()` method to calculate the **maximum absolute difference** between any two integers in the array.
3. Store the result in a public variable `maximumDifference`.

The main program (provided by HackerRank) will then print `maximumDifference`.

---

## 🧮 Example

**Input**
3
1 2 5

**Output**
4

**Explanation**
The maximum absolute difference is `|1 - 5| = 4`.

---

## 💡 Approach

- **Python**: Used `max()` and `min()` built-in functions to get the maximum and minimum element and find their difference in O(n) time.

---

## 🖥 Code Implementation (Python)
```python
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)


# Input handling for HackerRank
_ = input()
a = list(map(int, input().split()))

d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
