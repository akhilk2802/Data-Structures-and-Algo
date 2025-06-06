# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        '''
        brute force ->
        traverse each level, find the average
        '''

        result = []

        if not root:
            return result

        q = deque([root])

        while q:
            level = []
            for i in range(len(q)):
                root = q.popleft()
                level.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            
            result.append(sum(level)/len(level))
        return result

        