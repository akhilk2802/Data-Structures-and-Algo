# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        return self.isEqual(root.left, root.right)
        

    def isEqual(self, rootLeft, rootRight):
        if rootLeft == None and rootRight == None:
            return True
        if rootLeft == None or rootRight == None:
            return False
        if rootLeft.val != rootRight.val:
            return False
        return self.isEqual(rootLeft.left, rootRight.right) and self.isEqual(rootLeft.right, rootRight.left)