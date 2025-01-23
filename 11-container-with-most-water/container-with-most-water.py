class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = 0

        while right > left:
            width = right - left
            currentHeight = min(height[right], height[left])
            currentArea = width * currentHeight
            maxWater = max(maxWater, currentArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater

            
            