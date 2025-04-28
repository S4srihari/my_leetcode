class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        #90^
        #Transpose
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        #mirror
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        
        """# 180^
        # cols mirror
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        # rows mirror
        for i in range(n//2):
            matrix[i],matrix[n-i-1] = matrix[n-i-1],matrix[i]"""

        """#270^ or -90^
        # transpose
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #mirror rows
        for i in range(n//2):
            matrix[i],matrix[n-i-1] = matrix[n-i-1], matrix[i]"""