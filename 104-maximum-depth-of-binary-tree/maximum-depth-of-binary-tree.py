# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        height = 0

        def dfs(root):

            nonlocal height
            if not root:
                return 0

            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            max_height = max(left, right)
            height = 1 + max_height

            return height

        return dfs(root)