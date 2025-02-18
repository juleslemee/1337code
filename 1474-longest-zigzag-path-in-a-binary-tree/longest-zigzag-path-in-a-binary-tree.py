# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, direction, length):
            """ 
            direction = 0 -> came from left, now go right
            direction = 1 -> came from right, now go left
            """
            if not node:
                return
            
            # Update max length
            self.max_length = max(self.max_length, length)
            
            # If we came from left, go right
            if direction == 0:
                dfs(node.right, 1, length + 1)  # Continue zigzag
                dfs(node.left, 0, 1)  # Restart zigzag from left
            # If we came from right, go left
            else:
                dfs(node.left, 0, length + 1)  # Continue zigzag
                dfs(node.right, 1, 1)  # Restart zigzag from right
        
        if not root:
            return 0
        
        self.max_length = 0
        dfs(root.left, 0, 1)  # Start zigzag path going left
        dfs(root.right, 1, 1)  # Start zigzag path going right
        return self.max_length