# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        half = len(stack) // 2

        curr = head
        count = 0

        while count < half:
            tail_node = stack.pop()
            next_node = curr.next
            curr.next = tail_node
            tail_node.next = next_node

            curr = next_node
            count += 1

        if curr:
            curr.next = None

        # while curr:
        #     if len(stack) >= half:
        #         new_node = ListNode(stack.pop())
        #         next_node = curr.next
        #         curr.next = new_node
        #         new_node.next = next_node
        #     curr = curr.next
        
