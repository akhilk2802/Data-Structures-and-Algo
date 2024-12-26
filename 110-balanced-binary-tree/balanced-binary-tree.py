# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeightAndBalance(node):
            if not node:
                return 0  # Height of an empty tree is 0

            # Recursively get the height of left and right subtrees
            leftHeight = checkHeightAndBalance(node.left)
            if leftHeight == -1:  # Left subtree is unbalanced
                return -1

            rightHeight = checkHeightAndBalance(node.right)
            if rightHeight == -1:  # Right subtree is unbalanced
                return -1

            # Check if the current node is balanced
            if abs(leftHeight - rightHeight) > 1:
                return -1  # Current node is unbalanced

            # Return the height of the current node
            return 1 + max(leftHeight, rightHeight)

        # If the function returns -1, the tree is unbalanced
        return checkHeightAndBalance(root) != -1