class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        cols = set()
        for r in range(m):
            col = 0
            for val in matrix[r]:
                if val == 0:
                    matrix[r] = [0]*n
                    cols.add(col)
                col += 1
        if cols:
            for r in range(m):
                for col in cols:
                    matrix[r][col] = 0