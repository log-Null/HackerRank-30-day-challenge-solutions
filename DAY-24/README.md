# HackerRank 30 Days of Code — Day 24: More Linked Lists

## 📌 Problem
You are given a **sorted singly linked list**.  
Your task is to **remove consecutive duplicate values** so that each element appears only once.

Example:
Input:  1 -> 2 -> 2 -> 3 -> 3 -> 4
Output: 1 -> 2 -> 3 -> 4

## 🧠 Approach
- Since the list is **sorted**, duplicates will always be **next to each other**.
- Traverse the list using a pointer:
  - If the current node’s `data` equals the next node’s `data` → skip the next node.
  - Otherwise → move to the next node.
- Continue until the end of the list.



          

## 🚀 Example Run
Input
6
1 2 2 3 3 4

Output
1 2 3 4

##

