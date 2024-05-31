# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        if lenA > lenB:
            headA = self.advList(headA, lenA - lenB)
        else:
            headB = self.advList(headB, lenB - lenA)

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def advList(self, head, n):
        while n > 0 and head:
            head = head.next
            n -= 1
        return head
        