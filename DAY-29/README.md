# Day 29: Bitwise AND – 30 Days of Code (HackerRank)

## Problem Statement
We are given a set **S = {1, 2, 3, …, N}**.  
We need to choose two integers **A** and **B** (where A < B) such that:

- The value of `A & B` (bitwise AND) is **the maximum possible**, and  
- It is **strictly less than a given integer K**.  

We must output this maximum possible value for each test case.

---

## Input Format
- The first line contains an integer **T**, the number of test cases.  
- Each test case contains two space-separated integers:  
  - **N** → size of the set (1 to N).  
  - **K** → upper limit, the result of `A & B` must be < K.

---

## Sample Input
3
5 2
8 5
2 2

---

## Sample Output
1
4
0
