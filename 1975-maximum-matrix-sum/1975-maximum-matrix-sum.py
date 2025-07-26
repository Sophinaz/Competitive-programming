class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_number = float('inf')
        count_negative = 0
        n_row = len(matrix)
        n_col = len(matrix[0])
        total = 0

        for row in range(n_row):
            for col in range(n_col):
                value = matrix[row][col]
                total += abs(value)
                if value < 0:
                    count_negative += 1
                min_number = min(min_number, abs(value))
        if count_negative % 2:
            total -= (2 * min_number)

        return total