# Day 20: Sorting – 30 Days of Code.

## Problem Statement
Given an array of integers, sort the array in ascending order using **Bubble Sort** and print:
1. The number of swaps it took to sort the array.
2. The first element of the sorted array.
3. The last element of the sorted array.

---

## Input Format
- The first line contains an integer **n**, the size of the array.
- The second line contains **n** space-separated integers.

---

## Constraints
- \( 2 \leq n \leq 600 \)
- \( 1 \leq a_i \leq 2 \times 10^6 \)

---

## Output Format
Print the following three lines:

```
Array is sorted in numSwaps swaps.
First Element: firstElement
Last Element: lastElement
```

Where:
- `numSwaps` is the total number of swaps made.
- `firstElement` is the first element in the sorted array.
- `lastElement` is the last element in the sorted array.

---

## Sample Input
```
3
1 2 3
```

## Sample Output
```
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
```

---

## Explanation
The array is already sorted, so no swaps are needed.  
The first element is `1`, and the last element is `3`.

---

## Solution (Python 3)
```python
# Day 20: Sorting - 30 Days of Code (HackerRank)

n = int(input().strip())
a = list(map(int, input().rstrip().split()))

number_of_swaps = 0

# Bubble sort
for i in range(n):
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
```

---

