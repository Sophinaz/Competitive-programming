class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n= len(strs)
        m = len(strs[0])
        answer = [[0] * n for _ in range(len(strs[0]))]
        count =0
        
        for i in range(n):
            for j in range(len(strs[0])):
                answer[j][i] = strs[i][j]
        for i in range(len(answer)):
            for j in range(1,len(answer[0])):
                if answer[i][j] < answer[i][j-1]: 
                    count += 1
                    break
        return count
        