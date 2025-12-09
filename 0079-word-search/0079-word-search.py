class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        def valid(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def backtrack(row, col, idx, visited):
            if idx == len(word):
                return True
            visited.add((row, col))
            res = False
            for r, c in directions:
                new_row = row + r
                new_col = col + c
                if not valid(new_row, new_col) or (new_row, new_col) in visited:
                    continue

                if board[new_row][new_col] == word[idx]:
                    res = res or backtrack(new_row, new_col, idx + 1, visited)
            visited.remove((row, col))

            return res
        result = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    result = result or backtrack(i, j, 1, set())

        return result