\# Factorial Function – HackerRank Solution



This repository contains the solution for the \*\*"Factorial"\*\* problem from HackerRank's 30 Days of Code challenge.



\## 🚀 Problem Statement



Given an integer `n`, calculate and return the \*\*factorial\*\* of `n`. The factorial of `n` is the product of all positive integers less than or equal to `n`.  



Factorial is defined as:



factorial(0) = 1

factorial(n) = n × (n - 1) × (n - 2) × ... × 1



---



\## 📥 Input



\- A single integer `n` (0 ≤ n ≤ 12)



\## 📤 Output



\- A single integer: `n!` (the factorial of `n`)



---



\## 💡 Sample Input

5



---



\## 🔁 Example Explanation



5! = 5 × 4 × 3 × 2 × 1 = \*\*120\*\*



---



\## 🧠 Approach



\- Used a \*\*recursive function\*\* to compute the factorial.

\- If `n` is 0 or 1, return 1.

\- Otherwise, return `n × factorial(n - 1)`.



---



\## 📝 Language Used



\- Python 3



---



\## ALSO



This is part of my #30DaysOfCode journey. Check out the https://github.com/log-Null/HackerRank-30-day-challenge-solutions to follow my progress.

