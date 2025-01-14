class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        # result [] will be the 'victorystatus' of the ith children
        result = []
        # find the max in here
        maxlist = (sorted(candies, reverse=True))
        # take max - extraCandies
        toBeat = (maxlist[0] - extraCandies)
        for i in range(len(candies)):
            # all elements with this value or greater will have 'true'
            if candies[i] >= toBeat:
                result.append(True)
            else:
                result.append(False)
        return result


        