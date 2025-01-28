class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = count = 0
        maxSize = 0

        for r, num in enumerate(nums):
            if num==0:
                count += 1
            
            while count > 1:
                if nums[l]==0:
                    count -= 1
                l += 1

            maxSize = max(maxSize, r - l)

        return maxSize