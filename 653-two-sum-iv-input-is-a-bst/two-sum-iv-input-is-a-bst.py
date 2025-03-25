# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        arr = []

        def inorder(root):
            if root:
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)

        inorder(root)

        print("array : ", arr)
        m = {}

        for i, num in enumerate(arr):
            comp = k - num
            if comp in m:
                return True
            m[num] = i
        return False
        # l, r = 0, len(arr) - 1

        # while l < r:
        #     if arr[l] + arr[r] == k:
        #         return True
        #     if arr[l] + arr[r] > r:
        #         r -= 1
        #     else:
        #         l += 1

        # return False