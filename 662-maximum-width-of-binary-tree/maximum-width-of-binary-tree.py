# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = deque([(root, 1)])

        while queue:
            level_length = len(queue)
            _, first_pos = queue[0]
            for _ in range(level_length):
                node, pos = queue.popleft()
                pos -= first_pos
                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))
            
            if queue:
                current_width = queue[-1][1] - queue[0][1] + 1
            else:
                current_width = 1
            max_width = max(max_width, current_width)

        return max_width