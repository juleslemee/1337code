# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False
        
        list1 = self.traverse(root1)
        list2 = self.traverse(root2)

        if list1 == list2:
            return True
        else:
            return False

    def traverse(self, root) -> list:
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        leftSide = self.traverse(root.left)
        rightSide = self.traverse(root.right)

        return leftSide + rightSide
