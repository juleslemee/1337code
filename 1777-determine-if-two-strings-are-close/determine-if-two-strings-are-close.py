class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hash1 = {}
        hash2 = {}
        for char1 in word1:
            hash1[char1] = hash1.get(char1, 0) + 1
        for char2 in word2:
            hash2[char2] = hash2.get(char2, 0) + 1
        return sorted(list(hash1.keys())) == sorted(list(hash2.keys())) and sorted(list(hash1.values())) == sorted(list(hash2.values()))