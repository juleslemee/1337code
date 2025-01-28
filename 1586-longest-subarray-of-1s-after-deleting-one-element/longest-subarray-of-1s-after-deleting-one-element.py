class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = count = 0
        maxSize = 0

        for r, num in enumerate(nums):
            count += (1 if num==0 else 0)
            
            while count > 1:
                count -= (1 if nums[l]==0 else 0)
                l += 1

            maxSize = max(maxSize, r - l)

        return maxSize