class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [[0 for i in range(len(colSum))] for i in range(len(rowSum))]
        prefixrow = defaultdict(int)
        prefixcol = defaultdict(int)

        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                result[i][j] = min(rowSum[i] - prefixrow[i], colSum[j] - prefixcol[j])
                prefixrow[i] += result[i][j]
                prefixcol[j] += result[i][j]

        return result