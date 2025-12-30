class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # Brute Force
        """
        taking each possible 3X3 grid and checking is it magic ?
        Tc = O(rows*cols)
        sc = O(1)
        """
        # optimal
        """
        1. Distinct 1-9 -> set to look for distincts
        2. sum = 15 -> calculaing sums row, col wise, diagonal wise
        """
        def row_calc(row,col):
            distinct = set()
            magic = True
            for i in range(3):
                tot = 0
                for j in range(3):
                    tot += grid[row + i][col + j]
                    if grid[row+i][col+j] in distinct or grid[row+i][col+j] > 9 or grid[row+i][col+j] < 1:
                        magic = False
                        break
                    distinct.add(grid[row+i][col+j])
                if not magic or tot != 15:
                    magic = False
                    break
            return magic
        
        def col_calc(row,col):
            magic = True
            for j in range(3):
                tot = 0
                for i in range(3):
                    tot += grid[row + i][col + j]
                if tot != 15:
                    magic = False
                    break
            return magic
        
        def diag_calc(row,col):
            return grid[row+1][col+1] == 5

        rows, cols = len(grid), len(grid[0])
        cnt = 0
        for row in range(rows-2):
            for col in range(cols-2):
                if row_calc(row,col) and col_calc(row,col) and diag_calc(row,col):
                    cnt += 1
        return cnt