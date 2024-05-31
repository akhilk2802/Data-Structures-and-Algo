# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def getLength(self, head):
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length 

    def reverseInK(self, head, k, length):
        if k > length:
            return head 

        curr = head 
        prev = None 
        temp = None 
        count = 0

        while curr is not None and count < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        
        if temp is not None:
            head.next = self.reverseInK(temp, k, length-k)

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None:
            return None 
        
        length = self.getLength(head)
        return self.reverseInK(head, k, length)
        