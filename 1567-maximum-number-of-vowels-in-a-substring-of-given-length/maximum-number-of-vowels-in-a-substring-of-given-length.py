class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        maxvows = vows = 0

        for i in range(k):
            if s[i] in vowels:
                vows += 1
        maxvows = vows

        for i in range(k, len(s)):
            if s[i] in vowels:
                vows += 1
            if s[i-k] in vowels:
                vows -= 1
            maxvows = max(vows, maxvows)
        
        return maxvows