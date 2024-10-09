# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        tList = []
        self.inorder(root, tList)
        tList = sorted(tList)

        return tList[k-1]
        

    def inorder(self,root, tList):
        if root:
            self.inorder(root.left, tList)
            tList.append(root.val)
            self.inorder(root.right, tList)