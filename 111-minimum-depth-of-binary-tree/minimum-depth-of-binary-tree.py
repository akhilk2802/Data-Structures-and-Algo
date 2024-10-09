# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        depth = 1
        if not root:
            return 0

        queue = deque([root])

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if(node.left is None) and (node.right is None):
                    return depth
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                                    
            depth += 1

        return depth

        