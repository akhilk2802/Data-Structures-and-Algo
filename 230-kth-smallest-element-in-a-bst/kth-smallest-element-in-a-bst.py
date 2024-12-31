# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        Tlist = []
        self.inorder(root, Tlist)
        return Tlist[k-1]

    def inorder(self, root, Tlist):
        if root:
            self.inorder(root.left, Tlist)
            Tlist.append(root.val)
            self.inorder(root.right, Tlist)


