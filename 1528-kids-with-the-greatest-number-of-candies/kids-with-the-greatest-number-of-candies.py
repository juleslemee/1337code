class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        index is the child number. value is their number of candies
        :type extraCandies: int
        all the extras i have to give to the ith person
        :rtype: List[bool]
        """
        # result [] will be the 'victorystatus' of the ith children
        result = []
        for i in range(len(candies)):
            print(candies[i])
            # find the max in here
            maxlist = (sorted(candies, reverse=True))
            # take max - extraCandies
            toBeat = (maxlist[0] - extraCandies)
            # all elements with this value or greater will have 'true'
            if candies[i] >= toBeat:
                result.append(True)
            else:
                result.append(False)
        return result


        