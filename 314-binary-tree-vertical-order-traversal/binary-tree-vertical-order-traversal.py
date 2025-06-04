# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        c_map = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()

            c_map[col].append(node.val)

            if node.left:
                queue.append((node.left, col-1))
            if node.right:
                queue.append((node.right, col+1))


        sort_map = sorted(c_map.items(), key=lambda i:i[0])
        result = []

        for k, v in sort_map:
            result.append(v)

        return result