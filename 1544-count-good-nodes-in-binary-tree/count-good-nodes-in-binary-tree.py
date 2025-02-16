# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# basically, a node is good if nothing that comes before it on the way to traversal is greater than itself. 
# So I guess I would need to do some kind of DFS traversal, Root->left->right
# I would want to store the node and all the nodes that lead up to it. 

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countGoods(root)
    def countGoods(self, root, maxSoFar=float('-inf')):
        if root is None:
            return 0
        
        count = 1 if root.val >= maxSoFar else 0

        newMax = max(maxSoFar, root.val)

        count += self.countGoods(root.left, newMax)
        count += self.countGoods(root.right, newMax)
        
        return count