class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        grid_hash = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in row_hash[i] or board[i][j] in col_hash[j] or board[i][j] in grid_hash[(i//3,j//3)]:
                    return False
                else:
                    row_hash[i].add(board[i][j])
                    col_hash[j].add(board[i][j])
                    grid_hash[(i//3,j//3)].add(board[i][j])
        return True