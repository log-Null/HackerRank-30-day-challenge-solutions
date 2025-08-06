# 📘 Day 12: Inheritance – HackerRank 30 Days of Code

## 🔹 Problem Summary

This challenge focuses on **object-oriented programming** using **inheritance**.  
You're given a base class `Person`. Your task is to create a derived class `Student` that:
- Inherits from `Person`
- Contains an array of test scores
- Calculates and returns a letter grade based on average score

## 🔹 Concepts Used
- Object-Oriented Programming (OOP)
- Inheritance
- Method Overriding
- Use of `super()` in Python

---

## 🧠 Grade Calculation Logic

| Average Score | Grade                |
|---------------|----------------------|
| 90–100        | O (Outstanding)      |
| 80–89         | E (Exceeds Expectations) |
| 70–79         | A (Acceptable)       |
| 55–69         | P (Poor)             |
| 40–54         | D (Dreadful)         |
| < 40          | T (Troll)            |

---

## 🧾 Input Format

```
FirstName LastName ID
NumberOfScores
Score1 Score2 ... ScoreN
```

---

## 📎 Sample Input

```
Heraldo Memelli 8135627
2
100 80
```

---

## 📤 Sample Output

```
Name: Memelli, Heraldo
ID: 8135627
Grade: O
```

---

## ✅ How It Works

- A `Student` object is created with inherited attributes from `Person`
- The `calculate()` method computes the average of scores and maps it to a grade
- `printPerson()` prints the student's name and ID

---

## 🛠️ Tech Used

- Language: Python 3
- Concepts: Classes, Inheritance, Lists, Method Overriding

---

---

## Also:
This is part of my #30DaysOfCode journey. Check out the https://github.com/log-Null/HackerRank-30-day-challenge-solutions to follow my progress.




