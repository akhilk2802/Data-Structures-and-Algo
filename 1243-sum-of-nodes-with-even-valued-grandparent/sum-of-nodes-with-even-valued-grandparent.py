# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        sum = 0
        if not root:
            return 0
        
        queue = deque([(root, None, None)])
        while queue:
            node, parent, grandparent = queue.popleft()

            if grandparent and grandparent.val % 2 == 0:
                sum += node.val

            if node.left:
                queue.append((node.left, node, parent))
            if node.right:
                queue.append((node.right, node, parent))

        return sum
        