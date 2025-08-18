# Day 22: Binary Search Trees (HackerRank 30 Days of Code)

## Problem
You are given the task of building a binary search tree (BST) from `T` integers.  
After inserting all nodes, you must compute and print the **height of the tree**.

**Definition of Height**:
- The height of an empty tree is `-1`.
- The height of a leaf node is `0`.
- For any other node,  
  `height = 1 + max(height(left_subtree), height(right_subtree))`.

---

## Solution

```python
class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root is None:
            return -1   # base case: empty tree
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        return 1 + max(left_height, right_height)

# main
T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)

height = myTree.getHeight(root)
print(height)
```

---

## Example

### Input
```
7
3
5
2
1
4
6
7
```

### Tree Structure
```
        3
       / \
      2   5
     /   / \
    1   4   6
             \
              7
```

### Output
```
3
```


