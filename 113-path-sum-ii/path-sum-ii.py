# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        paths = []

        def dfs(root, current_sum, path):
            if not root:
                return
            path.append(root.val)
            current_sum += root.val
            if not root.left and not root.right and current_sum == targetSum:
                paths.append(path[:])
            else:
                dfs(root.left, current_sum, path)
                dfs(root.right, current_sum, path)
            path.pop()
        
        dfs(root, 0, [])
        return paths
        