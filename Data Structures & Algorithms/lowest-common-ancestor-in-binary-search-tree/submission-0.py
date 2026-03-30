# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # p or q are the root
        if p.val == root.val and self.contains(root, q.val):
            return root
        elif q.val == root.val and self.contains(root, p.val):
            return root
        
        # p,q are in left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
            
        # p,q are in right subtree
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # p in left, q in right
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            cond = (self.contains(root.left, p.val) and self.contains(root.right, q.val)) or \
                   (self.contains(root.left, q.val) and self.contains(root.right, p.val))

            if cond:
                return root
            

    def contains(self, root, val):
        # empty root is false
        if not root:
            return False
        
        # found val
        if root.val == val:
            return True

        # didn't find val, keep searching
        return self.contains(root.left, val) or self.contains(root.right, val)