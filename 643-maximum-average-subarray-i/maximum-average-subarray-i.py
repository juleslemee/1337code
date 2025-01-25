class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = 0
        currentLen = 1
        sumNums = nums[start]
        currentMax = sumNums / k
        while end < len(nums)-1:
            if currentLen < k:
                end += 1
                currentLen += 1
                sumNums += nums[end]
                currentMax = sumNums / k
            else:
                sumNums -= nums[start]
                start += 1
                end += 1
                sumNums += nums[end]
                avgNums = sumNums / k
                currentMax = max(avgNums, currentMax)

        return currentMax
