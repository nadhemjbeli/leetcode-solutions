from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:  
    # Time  — O(n * m): for each of n nodes in root, we potentially run 
    # isSameTree which is O(m)
    # Space — O(h): recursion depth of the main tree 
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if not root and not subRoot: return True
            if not root or not subRoot: return False
            isSameLeft = self.isSameTree(root.left, subRoot.left)
            isSameRight = self.isSameTree(root.right, subRoot.right)
            return root.val == subRoot.val and isSameLeft and isSameRight
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if self.isSameTree(root, subRoot): return True
        return (self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot))

# main test cases
if __name__ == "__main__":
    s = Solution()
    # tree: [3,4,5,1,2]
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    # tree: [4,1,2]
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    print(s.isSubtree(root, subRoot)) # -> True

    # tree: [3,4,5,1,2,null,null,null,null,0]
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)
    # tree: [4,1,2]
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    print(s.isSubtree(root, subRoot)) # -> False