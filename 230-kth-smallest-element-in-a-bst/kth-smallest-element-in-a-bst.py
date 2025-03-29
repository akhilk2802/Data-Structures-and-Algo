# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        '''
        very brute force approach will be adding the elements to the list and then sort it find the kth smallest
        '''

        kth_val = None
        count = 0

        def dfs(root):
            nonlocal kth_val, count
            if not root:
                return 
            dfs(root.left)
            count += 1
            if count == k:
                kth_val = root.val
                return
            dfs(root.right)
        
        dfs(root)
        return kth_val
