# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        hold = ListNode(-1)
        hold.next = head

        curr, prev = head, hold
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next
                
        return hold.next