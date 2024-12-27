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

        queue = deque([root])
        result = []
        depth = 0

        while queue:
            l = len(queue)
            level = []
            depth += 1
            for i in range(l):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print("l :", l)
            if depth % 2 == 0:
                level.reverse()
                print("l: , level: ", depth, level)
            result.append(level)

        return result
                
