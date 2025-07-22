class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[0,1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        def valid(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0]) 
        def live_neighbours(row, col):
            count = 0
            for r, c in directions:
                new_row = row + r
                new_col = col + c
                if valid(new_row, new_col) and (board[new_row][new_col] == 1 or board[new_row][new_col] == 'O'):
                    count += 1
            return count
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                count = live_neighbours(row, col)
                if board[row][col] == 1:
                    if count < 2:
                        board[row][col] = 'O'
                    elif count > 3:
                        board[row][col] = 'O'
                else:
                    if count == 3:
                        board[row][col] = 'P'
                        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 0
                elif board[row][col] == 'P':
                    board[row][col] = 1