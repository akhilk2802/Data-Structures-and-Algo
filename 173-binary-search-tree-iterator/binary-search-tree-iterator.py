# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.array = []
        self.curr_index = 0
        self.inorder(root)


    def inorder(self, root):
        if not root:
            return 
        self.inorder(root.left)
        self.array.append(root.val)
        self.inorder(root.right)
        

    def next(self) -> int:
        val = self.array[self.curr_index]
        self.curr_index += 1
        return val
        

    def hasNext(self) -> bool:
        return self.curr_index<=len(self.array)-1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()