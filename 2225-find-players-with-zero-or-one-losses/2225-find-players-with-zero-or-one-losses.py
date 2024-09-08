class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        track0 = {}
        track1 = {}
        ans1 = []
        ans2 = []
        for i,j in matches:
            if j not in track1:
                if j not in track0: track1[j] = 1
            else: 
                track1.pop(j)
                track0[j] = 1


        for i,j in matches:
            if i not in  track1 and i not in track0 and i not in ans1:
                ans1.append(i)
        ans2 = list(set(track1.keys()))
        ans1.sort()
        ans2 = sorted(ans2)

        return [ans1,ans2]