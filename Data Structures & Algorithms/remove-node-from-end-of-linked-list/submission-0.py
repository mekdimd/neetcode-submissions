# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
                ----------------

                  c     n
        [1, 2, 3, 4, 5, 6, 7]
                  s        f

        
        npos = 7, count = 4
        ----------------

            n     c     
        [1, 2, 3, 4, 5, 6, 7]
                  s        f
        
        n = 2, count = 4

        -----------------
         n
        [d, 1, 2]
         L  R

        [1]

        count = 2, npos = 1
        diff = 1

        """
        dummy = ListNode(0, head)
        # left starts at dummy (one before)
        left = dummy 
        
        # right is offset by n
        right = head
        for _ in range(n):
            right = right.next

        # move nodes
        while right:
            left, right = left.next, right.next

        # left will point to node - 1 spot back
        # remove node (will be one before removal)
        left.next = left.next.next

        # return head
        return dummy.next