class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num  # smallest so far
            elif num <= second:
                second = num  # second smallest so far
            else:
                # If we find a number larger than both first and second,
                # it means there's an increasing triplet
                return True
        
        return False
