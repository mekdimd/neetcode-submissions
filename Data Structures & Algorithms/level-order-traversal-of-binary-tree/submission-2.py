# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.levelOrderIter(root)
        # return self.levelOrderRec(root)
    
    def levelOrderIter(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        result = []
        
        while queue:
            # building nodes in current
            level = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                
                if node:
                    # add node to current level
                    level.append(node.val)
                    
                    # add neighbours 
                    # (pushing null nodes is fine, will be caught by if statement)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if level:
                result.append(level)

        return result

    def levelOrderRec(self, root):
        res = []

        def dfs(node, level):
            if not node:
                return
            
            if level == len(res):
                res.append([])
            
            res[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return res
