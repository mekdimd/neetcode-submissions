# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder: [root, root.left, ..., root.right]
        inorder:  [root.left, root.left,  ]

        ROOT, left, right
        preorder = [3, 9, 20,15,7]
        
                  Left, ROOT, right
        inorder =  [9,  3,  15,20,7]

        ans = 3,9,20,null,null,15,7]
        """

        # store as hashmap for O(1) lookup
        # inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(preorder, inorder):
            # base case
            if not inorder or not preorder:
                return None
            
            # get root
            root_val = preorder[0]
            root_idx = inorder.index(root_val)

            # split inorder
            inorder_left = inorder[:root_idx]   # size root_idx+1
            inorder_right = inorder[root_idx+1:]

            # split preorder
            preorder_left = preorder[1 : root_idx + 1]
            preorder_right = preorder[root_idx + 1 :]

            # create tree
            root = TreeNode(root_val)
            root.left = build(preorder_left, inorder_left)
            root.right = build(preorder_right, inorder_right)

            return root

        return build(preorder, inorder)
