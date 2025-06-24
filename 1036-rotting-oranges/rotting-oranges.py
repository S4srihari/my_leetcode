class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        m,n = len(grid), len(grid[0])
        cnt_one,cnt_two = 0,0 
        rotten_q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: cnt_one += 1
                if grid[i][j] == 2: 
                    cnt_two += 1
                    rotten_q.append((i,j))
        if cnt_one == 0 : return 0
        if cnt_two == 0 : return -1

        while rotten_q:
            minutes += 1
            l = len(rotten_q)
            for _ in range(l):
                xpos, ypos = rotten_q.pop(0)
                if xpos > 0 and grid[xpos-1][ypos] == 1:
                    grid[xpos-1][ypos] = 2
                    rotten_q.append((xpos-1,ypos))
                    cnt_one -= 1
                if xpos < m-1 and grid[xpos+1][ypos] == 1:
                    grid[xpos+1][ypos] = 2
                    rotten_q.append((xpos+1,ypos))
                    cnt_one -= 1
                if ypos < n-1 and grid[xpos][ypos+1] == 1:
                    grid[xpos][ypos+1] = 2
                    rotten_q.append((xpos,ypos+1))
                    cnt_one -= 1
                if ypos > 0 and grid[xpos][ypos-1] == 1:
                    grid[xpos][ypos-1] = 2
                    rotten_q.append((xpos,ypos-1))
                    cnt_one -= 1
                if cnt_one == 0:
                    return minutes

        if cnt_one : return -1