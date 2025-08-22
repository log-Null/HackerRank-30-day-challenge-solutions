# 30 Days of Code - Day 26: Nested Logic

## Problem Statement
You are given the actual and expected return dates for a library book. Calculate the fine based on the following rules:

- **No fine**: If the book is returned on or before the expected return date.
- **15 Hackos/day**: If the book is returned late but within the same calendar month and year.
- **500 Hackos/month**: If the book is returned late but within the same calendar year.
- **10000 Hackos**: If the book is returned after the expected year.

### Input Format
Two lines of input:

1. `d1 m1 y1` - The actual return date (day, month, year)
2. `d2 m2 y2` - The expected return date (day, month, year)

### Output Format
Print a single integer, the library fine.

---
