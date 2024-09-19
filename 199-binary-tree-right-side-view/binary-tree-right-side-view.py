# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        view = []
        self.traverseRight(root, 0, view)
        return view
        
    def traverseRight(self, root, depth, view):
        if root:
            if depth == len(view):
                view.append(root.val)
            
            self.traverseRight(root.right, depth + 1, view)
            self.traverseRight(root.left, depth + 1, view)