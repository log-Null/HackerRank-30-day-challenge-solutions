# Day 19: Interfaces

## Problem
You are given a class `AdvancedArithmetic` with the method:
```
divisorSum(n)
```
Write a class `Calculator` that implements this method. The `divisorSum` method should return the sum of all divisors of `n`.

In Python, since there is no formal `interface` keyword, we simulate it by creating a base class with a method that raises `NotImplementedError`, forcing subclasses to implement it.

---

## Function Description
**Method to implement**:  
```python
def divisorSum(self, n):
```
- **Parameters**:
  - `n` (int): The integer for which to find the sum of all divisors.
- **Returns**:
  - (int): The sum of all divisors of `n`.

---

## Input Format
- The first line contains a single integer `n`.

---

## Output Format
- The first line should be:
```
I implemented: AdvancedArithmetic
```
- The second line should be the sum of the divisors of `n`.

---

## Constraints
- `1 <= n <= 1000`

---

## Sample Input
```
6
```

## Sample Output
```
I implemented: AdvancedArithmetic
12
```

---

## Explanation
The divisors of `6` are:  
`1, 2, 3, 6`  
Sum = `1 + 2 + 3 + 6 = 12`

---


---

## How It Works
1. **AdvancedArithmetic** acts as an interface with an unimplemented `divisorSum` method.  
2. **Calculator** inherits from `AdvancedArithmetic` and implements `divisorSum`.  
3. The method iterates from 1 to `n` and adds numbers that divide `n` evenly.  
4. The sum is returned and printed alongside the interface name.



