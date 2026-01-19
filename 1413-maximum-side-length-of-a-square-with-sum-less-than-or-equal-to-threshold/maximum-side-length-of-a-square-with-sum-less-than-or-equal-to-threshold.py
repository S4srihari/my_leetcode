class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        max_len = 0
        rows, cols = len(mat), len(mat[0])

        def find(i,j):
            if mat[i][j] > threshold:
                return 0
            tot = mat[i][j]
            siz = 1
            while tot <= threshold:
                if i+siz == rows or j+siz == cols:
                    break
                for r in range(i,i+siz+1):
                    tot += mat[r][j+siz]
                for c in range(j,j+siz):
                    tot += mat[i+siz][c]
                if tot > threshold:
                    break
                
                siz += 1
            
            return siz

        for r in range(rows):
            for c in range(cols):
                siz = find(r,c)
                max_len = max(max_len, siz)
        return max_len