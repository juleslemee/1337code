class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):  # Quick exit
            return False

        hash1, hash2 = {}, {}

        for i in range(len(word1)):
            hash1[word1[i]] = hash1.get(word1[i], 0) + 1
            hash2[word2[i]] = hash2.get(word2[i], 0) + 1

        if hash1.keys() != hash2.keys():
            return False

        return sorted(hash1.values()) == sorted(hash2.values())