class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        toBeat = max(candies) - extraCandies
        return [candy >= toBeat for candy in candies]


        