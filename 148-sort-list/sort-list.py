# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        brute force approach ->
        traverse the ll and create an array -> T - O(n), S - O(n)
        sort the array -> T - O(n log n)
        create a new ll and return -> T - O(n), S - O(n)

        Optimised approach ->
        using Merge Sort
        '''

        if not head or not head.next:
            return head
        
        def get_middle(head):
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(list1, list2):
            dummy = ListNode(0)
            tail = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next

                tail = tail.next
            tail.next = list1 or list2
            return dummy.next



        mid = get_middle(head)
        right = mid.next

        mid.next = None

        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right)

        return merge(left_sorted, right_sorted)

