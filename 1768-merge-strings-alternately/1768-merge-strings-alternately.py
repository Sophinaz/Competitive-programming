class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        if len(word1) > len(word2):
            boo = True
        else:
            boo = False
        word = zip(word1,word2)
        for i,j in word:
            result += i
            result += j
        if boo:
            result += word1[len(word2):]
        else:
            result += word2[len(word1):]
        return result