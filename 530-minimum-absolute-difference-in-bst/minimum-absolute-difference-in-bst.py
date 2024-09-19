# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        output = []
        self.inorder(root, output)
        min_diff = float('inf')
        for i in range(1, len(output)):
            min_diff = min(min_diff, output[i]-output[i-1])
        return min_diff

    def inorder(self, root, output):
        if root:
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)

        