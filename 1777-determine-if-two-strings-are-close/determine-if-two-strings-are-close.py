class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # swap any two existing characters and/or swap all of one char with another
        # so what's interesting is the characters. That's what we can change
        # with a hashmap, we can store the char and count as key:val. does position matter?
        # given all the modifications we can make, we just need to check that it has
        #  both the right characters and the right counts (independently)
        hash1 = {}
        hash2 = {}
        for char1 in word1:
            if char1 in hash1:
                hash1[char1] += 1
            else:
                hash1[char1] = 1
        for char2 in word2:
            if char2 in hash2:
                hash2[char2] += 1
            else:
                hash2[char2] = 1
        if sorted(list(hash1.keys())) == sorted(list(hash2.keys())) and sorted(list(hash1.values())) == sorted(list(hash2.values())):
            return True
        else:
            return False