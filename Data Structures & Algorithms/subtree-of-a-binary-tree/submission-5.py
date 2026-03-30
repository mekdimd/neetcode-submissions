# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
TIME COMPLEXITY: O(n * m)
In the worst case, you do an O(m) comparison at every node of root (n nodes):

SPACE COMPLEXITY: O(max(height(root), height(subRoot)))
max traversal is depth of whichever tree is larger

"""
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if root node is empty, we can't find any subtrees inside it
        # for this question: subroot guaranteed to have >1 elements
        if not root:
            return False
        
        # an empty subtree is a subtree of any tree
        if not subRoot:
            return True
        
        # case 1: root == subRoot (equivalent)
        # case 2: left subtree == subroot (recursive call)
        # case 3: right subtree == subRoot (recursive call)
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