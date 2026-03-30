# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Inorder traversal
        O(N) time, O(N) space
        """
        self.count = 0
        self.ans = None

        # build tree as sorted array
        def inOrder(root):
            if root is None or self.ans:
                return

            # visit left
            inOrder(root.left)
            
            # visit node
            self.count += 1
            if self.count == k:
                self.ans = root.val
                return

            # visit right
            inOrder(root.right)

        inOrder(root)

        return self.ans