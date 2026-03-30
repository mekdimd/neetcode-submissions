# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # If any node is missing, we can’t compute the LCA
        if not root or not p or not q:
            return None
        
        # if the larger one is on the left side, then both are on left side
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        
        # if the smaller one is on the right side, then both are on right side
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        
        # all other cases, root is a LCA
        else:
            return root