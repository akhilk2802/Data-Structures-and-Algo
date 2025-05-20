# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return []

        pointer1, pointer2 = head, head

        for _ in range(n):
            pointer1 = pointer1.next
        
        if pointer1:
            print("pointer1 value -> ", pointer1.val)
            print("pointer2 value -> ", pointer2.val)

        if not pointer1:
            return head.next

        while pointer1 and pointer1.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        pointer2.next = pointer2.next.next

        return head