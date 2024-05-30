# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr1 = head
        ptr2 = head

        while(ptr1 != None and ptr1.next != None):
            ptr2 = ptr2.next
            ptr1 = ptr1.next.next
        
        return ptr2
        