# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, currSum):
            if not node:
                return 0
            
            currSum += node.val
            count = prefixSum.get(currSum - targetSum, 0)
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1

            count += dfs(node.left, currSum)
            count += dfs(node.right, currSum)

            prefixSum[currSum] -= 1
            if prefixSum[currSum] == 0:
                del prefixSum[currSum]
            
            return count
        
        prefixSum = {0: 1}
        return dfs(root, 0)