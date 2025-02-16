# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, maxSoFar=float('-inf')) -> int:
        if root is None:
            return 0
        count = 1 if root.val >= maxSoFar else 0
        newMax = max(maxSoFar, root.val)
        count += self.goodNodes(root.left, newMax)
        count += self.goodNodes(root.right, newMax)
        return count