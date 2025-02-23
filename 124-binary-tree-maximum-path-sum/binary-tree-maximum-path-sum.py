# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_sum = float("-inf")

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            leftSum = max(dfs(node.left), 0)
            rightSum = max(dfs(node.right), 0)

            current_sum = node.val + leftSum + rightSum

            max_sum = max(max_sum, current_sum)

            return node.val + max(leftSum, rightSum)

        dfs(root)
        return max_sum
                
        