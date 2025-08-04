\# 🧠 HackerRank 30 Days of Code – Day 10: Binary Numbers



\## ✅ Goal:

Given an integer `n`, convert it to binary and print the \*\*maximum number of consecutive 1s\*\* in the binary representation.



---



\## 🧾 Input Format:

A single integer `n`.



\### 🔹 Constraints:

\- 1 ≤ n ≤ 10^6



---



\## 📌 Example:



\*\*Input:\*\*

```

13

```



\*\*Step 1:\*\* Convert to Binary:

```

13 in binary = 1101

```



\*\*Step 2:\*\* Find maximum consecutive 1s:

```

Binary: 1101 → has "11" and "1" → Max consecutive 1s = 2

```



\*\*Output:\*\*

```

2

```



---



\## 💡 Concept Explained:



1\. Use Python's built-in `bin()` to convert to binary:

```python

bin(13)  # output: '0b1101'

```



2\. Use `\[2:]` to remove the `'0b'` prefix:

```python

binary = bin(n)\[2:]

```



3\. Split the binary string wherever there is a `'0'`:

```python

binary.split('0')  # gives list of 1s like \['11', '1']

```



4\. Use `max()` on the lengths of those 1s:

```python

max(len(s) for s in binary.split('0'))

```



---



\## ✅ Final Code (Python):

```python

n = int(input())

binary = bin(n)\[2:]

max\_ones = max(len(s) for s in binary.split('0'))

print(max\_ones)

```



---



\## 🧪 Test Cases:



| Input | Binary     | Max Consecutive 1s |

|-------|------------|--------------------|

| 5     | 101        | 1                  |

| 6     | 110        | 2                  |

| 13    | 1101       | 2                  |

| 439   | 110110111  | 3                  |



---



\## ALSO:

This is part of my #30DaysOfCode journey. Check out the https://github.com/log-Null/HackerRank-30-day-challenge-solutions to follow my progress.

