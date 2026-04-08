from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr: return[True, 0]
            right = dfs(curr.right)
            left = dfs(curr.left)
            balanced = (left[0] and right[0] and
                    abs(left[1] - right[1]) <= 1)
            return[balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
    
# main test cases
if __name__ == "__main__":
    s = Solution()
    # tree: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.isBalanced(root)) # -> True

    # tree: [1,2,2,3,3,null,null,4,4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    print(s.isBalanced(root)) # -> False

    # tree: []
    print(s.isBalanced(None)) # -> True