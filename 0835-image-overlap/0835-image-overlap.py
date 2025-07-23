class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ones = []
        track = defaultdict(int)
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1: 
                    ones.append([i,j])
        for i in range(len(img2)):
            for j in range(len(img2[0])):
                if img2[i][j] == 1:
                    for a, b in ones:
                        diff = (i - a, j - b)
                        track[diff] += 1
        maxx = 0
        for i in track:
            if track[i] > maxx:
                maxx = track[i]
        return maxx
        