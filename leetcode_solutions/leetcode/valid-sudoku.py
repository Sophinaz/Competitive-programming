class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        containerj = defaultdict(set)
        container = defaultdict(set)
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] == '.': continue
                num = int(board[i][j])
                if num not in row: row.add(num)
                else: return False

                if num not in containerj[j]:
                    containerj[j].add(num)
                else: return False

                if num not in container[(i//3,j//3)]: container[(i//3,j//3)].add(num)
                else: return False
  
                
        return True
