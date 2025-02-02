class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        hash1 = {}
        hash2 = {}
        for char in word1:
            hash1[char] = hash1.get(char, 0) + 1
        for char in word2:
            hash2[char] = hash2.get(char, 0) + 1

        if set(hash1.keys()) != set(hash2.keys()):
            return False

        counth1 = {}
        counth2 = {}
        for count in hash1.values():
            counth1[count] = counth1.get(count, 0) + 1
        for count in hash2.values():
            counth2[count] = counth2.get(count, 0) + 1

        return counth1 == counth2