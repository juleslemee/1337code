class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # make a dict and put the list in, incrementing the value of the key(indexes in list)
        # extract values into a set
        # if the set length is shorter than the dict, it's False.
        countOccurances = {}
        for val in arr:
            if val in countOccurances:
                countOccurances[val] += 1
            else:
                countOccurances[val] = 1
        validator = set(countOccurances.values())
        if len(validator) < len(countOccurances):
            return False
        else:
            return True
