class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        n = len(mat[0])-1
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j: 
                    result += mat[i][j]
                    continue
                elif j == n and i != j:
                    result += mat[i][j]
            n -= 1
        return result

        