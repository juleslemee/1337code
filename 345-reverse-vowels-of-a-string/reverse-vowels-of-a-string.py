class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','A','e','E','i','I','o','O','u','U']
        chars = list(s)
        foundVowels = []
        for letter in s:
            if letter in vowels:
                foundVowels.append(letter)
        foundVowels = list(reversed(foundVowels))
        i = 0
        j = 0
        for letter in s:
            if letter in vowels:
                chars[i] = foundVowels[j]
                j += 1
            i += 1
        return ''.join(chars)