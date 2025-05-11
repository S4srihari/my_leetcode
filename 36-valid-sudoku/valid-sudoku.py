class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for j in range(9):
            # row condition
            d = {}
            for i in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] in d:
                    return False
                else :
                    d[board[j][i]] = 1
            print(d)
            # col condition
            d = {}
            for i in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in d:
                    return False
                else :
                    d[board[i][j]] = 1
        
        for i in range(9):
            d = {}
            for j in range(3):
                for k in range(3):
                    if board[(i//3)*3 + j][(i%3)*3 + k] == '.':
                        continue
                    elif board[(i//3)*3 + j][(i%3)*3 + k] in d:
                        return False
                    else :
                        d[board[(i//3)*3+j][(i%3)*3 + k]] = 1
        
        return True
