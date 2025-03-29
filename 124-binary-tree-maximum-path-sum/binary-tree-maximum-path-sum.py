# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_sum = float("-inf")

        def max_gain(root):
            nonlocal max_sum

            if not root:
                return 0

            left_gain = max(max_gain(root.left), 0)
            right_gain = max(max_gain(root.right), 0)

            gain_newPath = root.val + left_gain + right_gain
            max_sum = max(max_sum, gain_newPath)

            return root.val + max(left_gain, right_gain)
        
        max_gain(root)
        return max_sum

