class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        result = [0] * n
        track = {}
        for i in range(n):
            track[score[i]] = i
        
        score.sort(reverse = True)
        temp = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        for i in range(3):
            if i < n:result[track[score[i]]] = temp[i]
        for i in range(3,n):
            result[track[score[i]]] = str(i+1)

        return result