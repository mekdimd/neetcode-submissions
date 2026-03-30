# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        """
        1 -> 2 -> 3 -> 4 -> 5

        APPROACH, reverse 2nd half and merge
        Note that the list is split
            1 -> 2 -> 3 |  4 <- 5
                      ^    ^
                     mid  second
               
               NOTE: dont reverse 'mid'

        O(N) runtime, O(1) space
        """

        if not head or not head.next:
            return

        # find end pointer
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split list
        second = slow.next
        slow.next = None

        # reverse 2nd half of list 
        prev = None
        while second:
            next = second.next
            second.next = prev
            
            # update pointers
            prev = second
            second = next

        # merge 2 lists
        start, end = head, prev
        while end:
            temp_start, temp_end = start.next, end.next
            start.next = end
            end.next = temp_start

            # update pointers
            start, end = temp_start, temp_end
