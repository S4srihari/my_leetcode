class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        vals = defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i-1,j-1) not in vals:
                    vals[(i,j)] = matrix[i][j]
                elif vals[(i-1,j-1)] != matrix[i][j]:
                    return False
                else:
                    vals[(i,j)] = matrix[i][j]
        return True