# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        result = []

        curr_level = 0
        
        while queue:
            # building nodes in current
            result.append([])

            for _ in range(len(queue)):
                node = queue.pop(0)
                
                # add node to current level
                result[curr_level].append(node.val)
                
                # enqueue neighbours
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            # increment level for next iteration
            curr_level += 1

        return result