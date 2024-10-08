# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(0)
        tail = head

        while list1 != None and list2 != None:

            if list1.val < list2.val:
                tail.next = list1
                list1, tail = list1.next, list1
            else:
                tail.next = list2
                list2, tail = list2.next, list2

        if list1 or list2:
            tail.next = list1 if list1 else list2

        return head.next
        