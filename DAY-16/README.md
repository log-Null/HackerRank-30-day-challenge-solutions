# Day 16: Exceptions - String to Integer

## Problem Statement
Given a string `S`, convert it to an integer.  
If `S` cannot be converted to an integer, print `"Bad String"` instead.

### Input Format
- A single string, `S`.

### Output Format
- The integer representation of `S`, or `"Bad String"` if it cannot be converted.

### Sample Input 0
```
3
```

### Sample Output 0
```
3
```

### Sample Input 1
```
za
```

### Sample Output 1
```
Bad String
```

---


---

## Explanation
- **`try` block** attempts to convert the input to an integer using `int(S)`.
- If successful, the integer is printed.
- If a `ValueError` occurs (e.g., input is non-numeric), the program prints `"Bad String"`.

