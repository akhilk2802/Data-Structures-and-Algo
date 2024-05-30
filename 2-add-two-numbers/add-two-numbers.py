# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            d1 = l1.val if l1 is not None else 0
            d2 = l2.val if l2 is not None else 0

            sum = d1 + d2 + carry
            d = sum % 10
            carry = sum // 10

            new = ListNode(d)
            tail.next = new
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = head.next
        head.next = None
        return result
        