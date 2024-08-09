# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None
        
        node = head 
        curr = head 

        for i in range(n):
            curr = curr.next

        if not curr:
            return head.next

        while curr.next:
            node = node.next 
            curr = curr.next 

        node.next = node.next.next

        return head


        