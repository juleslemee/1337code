class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = maxOnes = 0 # save room declaring vars

        for r, num in enumerate(nums):
            k -= 1 - num # if num == 1, we don't want to take

            if k < 0:
                k += 1 - nums[l] # if l value in nums = 1, we don't want to take
                l += 1
            
            else:
                maxOnes = max(maxOnes, r - l +1)
        
        return maxOnes