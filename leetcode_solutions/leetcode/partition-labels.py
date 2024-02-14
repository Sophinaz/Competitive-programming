class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        count = {}
        result = []
        maxx,left = 0,0
        for i in range(len(s)):
            count[s[i]] = i

        for i in range(n):
            maxx = max(maxx,count[s[i]])
            if i == maxx:
                result.append(i-left+1)
                left = i + 1
                maxx = 0

        return result


         
