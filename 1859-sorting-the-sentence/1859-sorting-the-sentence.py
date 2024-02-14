class Solution:
    def sortSentence(self, s: str) -> str:
        s = list(map(str, s.split()))
        s = sorted(s, key = lambda x: x[-1])
        result = ""
        for i in s:
            i = i[:len(i)-1]
            result += i + " "
        return result[:len(result)-1]