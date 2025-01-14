class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        # result [] will be the 'victorystatus' of the ith children
        result = []
        for i in range(len(candies)):
            # all elements with this value or greater will have 'true'
            if candies[i] >= (max(candies) - extraCandies):
                result.append(True)
            else:
                result.append(False)
        return result


        