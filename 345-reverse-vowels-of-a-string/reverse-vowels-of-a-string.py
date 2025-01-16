class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','A','e','E','i','I','o','O','u','U'}
        # list will make it easier to traverse
        chars = list(s)
        # left is the beginning, right is the end (index starts at 0, so len-1)
        left, right = 0, len(chars)-1
        # until we've finished iterating from both sides and the pointers cross
        while left < right:
            # if left not in vowels, we can move it forward
            while left < right and chars[left] not in vowels:
                left += 1
            # if right not in vowels, we can move it back 
            while left < right and chars[right] not in vowels:
                right -= 1
            # once they are both in vowels, we'll swap them and increment both (+ & -)
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        # we need to get the list back into a string, no separator needed
        return ''.join(chars)