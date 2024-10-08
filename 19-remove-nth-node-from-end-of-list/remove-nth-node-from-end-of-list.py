# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None

        p1 = head 
        p2 = head

        for i in range(n):
            p1 = p1.next 

        if not p1:
            return head.next

        while p1.next:
            p2 = p2.next
            p1 = p1.next

        p2.next = p2.next.next

        return head     