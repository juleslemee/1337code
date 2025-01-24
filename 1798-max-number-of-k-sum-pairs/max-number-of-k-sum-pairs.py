class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashMap = {}
        maxOperations = 0
        for num in nums:
            complement = k - num
            if hashMap.get(complement, 0) > 0:
                maxOperations += 1
                hashMap[complement] -= 1
            else:
                hashMap[num] = hashMap.get(num, 0) + 1
            
        return maxOperations
            