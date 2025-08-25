class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        edgePos = set()
        rows,cols = len(board), len(board[0])

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(row,col):
            edgePos.add((row,col))
            for dr,dc in dirs:
                if 0 <= row+dr < rows and 0 <= col+dc < cols and board[row+dr][col+dc] == "O" and (row+dr,col+dc) not in edgePos:
                    dfs(row+dr,col+dc)
            return
        
        for r in range(rows):
            if board[r][0] == "O" and (r,0) not in edgePos:
                dfs(r,0)
            if board[r][cols-1] == "O" and (r,cols-1) not in edgePos:
                dfs(r,cols-1)
        
        for c in range(cols):
            if board[0][c] == "O" and (0,c) not in edgePos:
                dfs(0,c)
            if board[rows-1][c] == "O" and (rows-1,c) not in edgePos:
                dfs(rows-1,c)


        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row,col) not in edgePos :
                    board[row][col] = "X"
        