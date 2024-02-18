class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0

        gpointer,spointer = 0,0
        while gpointer < len(g) and spointer < len(s):
            if g[gpointer] <= s[spointer]:
                result += 1
                gpointer += 1
            
            spointer += 1

        return result