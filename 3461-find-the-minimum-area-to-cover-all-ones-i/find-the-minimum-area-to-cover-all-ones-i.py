class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top,bottom,left,right = None,None,None,None
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if top == None : top = i
                    if left == None  or left > j: left = j
                    if right == None or right < j: right = j
                    if bottom == None or bottom < i: bottom = i
        return (bottom-top+1)*(right-left+1)