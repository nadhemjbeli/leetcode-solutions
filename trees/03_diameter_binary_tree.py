from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, right+left)
            return 1 + max(left, right)
        dfs(root)
        return self.res

# main test cases
if __name__ == "__main__":
    s = Solution()
    # tree: [1,2,3,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(s.diameterOfBinaryTree(root)) # -> 3

    # tree: [1,2]
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(s.diameterOfBinaryTree(root)) # -> 1