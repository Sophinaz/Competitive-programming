class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        surplus = 0
        n = len(arr)
        track = {}
        maxx = 0

        for i in arr: 
            if i > n: surplus += 1
            if i not in track: track[i] = 0
            else: track[i] += 1
        for i in range(n,0,-1):
            if i not in track:
                if surplus > 0: 
                    maxx = max(maxx,i)
                    surplus -= 1
                else:
                    maxx = max(maxx,i)
                    maxx -= 1
            else:
                surplus += track[i]
                maxx = max(maxx,i)
        return maxx

                
