class Solution(object):
    def mergeAlternately(self, word1, word2):
        i1 = 0
        i2 = 0
        newword = []
        if len(word1) > len(word2):
            for i in (range(1, len(word1)+1)):
                if i1 < len(word1):
                    newword.append(word1[i1])
                    i1 += 1
                if i2 < len(word2):
                    newword.append(word2[i2])
                    i2 += 1
        else:
            for i in (range(1, len(word2)+1)):
                if i1 < len(word1):
                    newword.append(word1[i1])
                    i1 += 1
                if i2 < len(word2):
                    newword.append(word2[i2])
                    i2 += 1
        return ''.join(newword)