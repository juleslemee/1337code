class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        countS = 0
        i = 0
        end = len(t)-1

        if len(s) == 0:
            return True

        while i <= end and countS <= (len(s)-1):
            if s[countS] == t[i]:
                countS += 1
                i += 1
            else:
                i += 1

        if countS == len(s):
            return True
        else:
            return False

# want to check if s will be in t
# check if s[countS] is in t
# if yes, increment countS, indicating that we found the next value

# at the end, if countS = len(s), we traversed all in order successfully