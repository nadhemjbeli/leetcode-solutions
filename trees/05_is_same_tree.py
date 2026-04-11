from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity - O(n): each node of the two trees is accessed only once
    # Space complexity - O(h): recursion call stack depth equals tree height h
    # O(log n) balanced tree, O(n) worst case skewed tree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q or not p and q:
            return False
        isSameLeft = self.isSameTree(p.left, q.left)
        isSameRight = self.isSameTree(p.right, q.right)
        return p.val == q.val and isSameLeft and isSameRight

# main test cases
if __name__ == "__main__":
    s = Solution()
    # tree: [1,2,3]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    # tree: [1,2,3]
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(s.isSameTree(p, q)) # -> True

    # tree: [1,2]
    p = TreeNode(1)
    p.left = TreeNode(2)
    # tree: [1,null,2]
    q = TreeNode(1)
    q.right = TreeNode(2)
    print(s.isSameTree(p, q)) # -> False

    # tree: []
    p = None
    q = None
    print(s.isSameTree(p, q)) # -> True