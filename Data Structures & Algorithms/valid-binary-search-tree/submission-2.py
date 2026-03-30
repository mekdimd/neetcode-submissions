# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, left, right):
            # empty BST is valid
            if not root:
                return True
            
            # check current range
            if not left < root.val < right:
                return False

            # left < ... < root.val (left side)
            # root.val < ... < right (right side)
            return valid(root.left, left, root.val) and valid(root.right, root.val, right)
            
        return valid(root, float("-inf"), float("inf"))