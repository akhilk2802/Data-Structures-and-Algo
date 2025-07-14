# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:

        number = ""
        while (head):
            number += str(head.val)
            head = head.next
        
        print(number)
        return int(number, 2)
