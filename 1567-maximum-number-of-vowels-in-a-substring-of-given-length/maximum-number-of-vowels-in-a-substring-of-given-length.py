class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        start = 0
        end = 0
        curlen = 1
        vows = 0
        i = 0
        if s[start] in vowels:
            vows += 1
        maxvows = vows
        while end < len(s)-1:
            if curlen < k:
                end += 1
                if s[end] in vowels:
                    vows += 1
                curlen += 1
                maxvows = vows

            else:
                start += 1
                if s[start-1] in vowels:
                    vows -= 1
                end += 1
                if s[end] in vowels:
                    vows += 1
                maxvows = max(vows, maxvows)
            
        return maxvows