# Day 23: BST Level-Order Traversal (HackerRank 30 Days of Code)

## Problem
You are given a binary search tree (BST).  
Perform a **level-order traversal** (also known as BFS).  
Print all the nodes in a single line, separated by spaces.

---

## Explanation

- **Level-order traversal** visits nodes level by level from left to right.  
- We use a **queue** to store nodes while traversing.  
- Steps:
  1. Start with the root in the queue.
  2. Pop from the front of the queue.
  3. Print the node’s value.
  4. Push its left child (if exists).
  5. Push its right child (if exists).
  6. Repeat until queue is empty.

---

## Solution

```python
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        if root is None:
            return
        queue = [root]   # initialize queue with root
        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

# main
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
```

---

## Example

### Input
```
6
3
5
4
7
2
1
```

### BST Structure
```
       3
      / \
     2   5
    /   / \
   1   4   7
```

### Output
```
3 2 5 1 4 7
```

---


