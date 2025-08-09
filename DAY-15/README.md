# Day 15 - 30 Days of Code: Linked List 

## Problem Statement

Implement a singly linked list by completing the following tasks:

- Define a `Node` class to represent each element of the linked list.
- Implement an `insert` method to add a new node with given data at the tail (end) of the linked list.
- Implement a `display` method to print all the elements of the linked list in order.

---

## Approach

- The `Node` class contains two properties: 
  - `data`: to store the value of the node
  - `next`: a pointer/reference to the next node (initially `None`)
- The `insert` method:
  - Creates a new node with the given data.
  - If the list is empty (`head` is `None`), the new node becomes the head.
  - Otherwise, traverse the list to the last node and attach the new node.
- The `display` method:
  - Traverses the linked list from the head and prints the data of each node, separated by spaces.

---

## ALSO:
This is part of my #30DaysOfCode journey. Check out the https://github.com/log-Null/HackerRank-30-day-challenge-solutions to follow my progress.

---

## Usage

To use the code:

1. Initialize `head` as `None`.
2. For each value you want to insert, call the `insert` method to add it to the list.
3. Call the `display` method to print the linked list.

Example:

mylist = Solution()
head = None

for _ in range(int(input())):
    data = int(input())
    head = mylist.insert(head, data)

mylist.display(head)

---

## Input Format

- The first line contains an integer `N` denoting the number of elements to insert.
- The next `N` lines each contain an integer, the data for each node.

---

## Output Format

- The linked list elements printed in a single line, separated by spaces.

---

## Sample Input

4
2
3
4
1

## Sample Output

2 3 4 1

