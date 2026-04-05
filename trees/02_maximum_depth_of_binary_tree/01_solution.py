from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # recursive DFS
    # Time - O(n) looping through each node of the tree
    # Space - O(h): recursion call stack depth equals tree height h 
    # O(log n) for balanced tree, O(n) worst case for skewed tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
# main test cases
if __name__ == "__main__":
    s = Solution()
    # tree: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.maxDepth(root)) # -> 3

    # tree: [1,null,2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(s.maxDepth(root)) # -> 2

    # tree: []
    print(s.maxDepth(None)) # -> 0