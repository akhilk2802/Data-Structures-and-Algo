# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cameras = 0
        
        # Helper DFS that returns the state of the node.
        # 0: not covered, 1: covered (no camera), 2: has camera.
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                # A null node is considered covered.
                return 1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If any child is not covered, place a camera at this node.
            if left == 0 or right == 0:
                self.cameras += 1
                return 2
            
            # If any child has a camera, this node is covered.
            if left == 2 or right == 2:
                return 1
            
            # Otherwise, this node is not covered.
            return 0
        
        # Start DFS from root.
        if dfs(root) == 0:
            self.cameras += 1
        
        return self.cameras
        