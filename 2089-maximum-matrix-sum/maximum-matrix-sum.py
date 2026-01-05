class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        negs = 0
        mini = float("inf")
        tot = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] < 0:
                    negs += 1
                tot += abs(matrix[row][col])
                if abs(matrix[row][col]) < mini:
                    mini = abs(matrix[row][col])
        if negs%2 == 0:
            return tot
        else:
            return tot - mini*2
        