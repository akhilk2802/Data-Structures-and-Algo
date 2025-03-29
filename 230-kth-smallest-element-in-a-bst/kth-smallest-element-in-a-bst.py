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
        l = []
        def dfs(root):
            if not root:
                return 
            l.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        l.sort()
        print("list -> ", l)
        return l[k-1]
        
            