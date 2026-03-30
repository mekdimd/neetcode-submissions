# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return not subRoot
        
        if not subRoot:
            return False
        
        # current root is subroot
        return self.isEquiv(root, subRoot) or \
        self.isSubtree(root.left, subRoot) or \
        self.isSubtree(root.right, subRoot)

    def isEquiv(self, p, q):
        if not p:
            return not q
        if not q:
            return not p
        
        return p.val == q.val \
        and self.isEquiv(p.left, q.left) \
        and self.isEquiv(p.right, q.right)