# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result = []
        q = deque([root])
        depth = 0

        while q:

            depth += 1
            level_size = len(q)
            level_nodes = []

            for _ in range(level_size):

                node = q.popleft()
                level_nodes.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if depth % 2 == 0:
                level_nodes.reverse()

            result.append(level_nodes)

        return result
                

