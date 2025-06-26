class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        m,n = len(grid), len(grid[0])
        cnt_fresh = 0 
        rotten_q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: cnt_fresh += 1
                if grid[i][j] == 2: 
                    rotten_q.append((i,j))
        if cnt_fresh == 0 : return 0

        while rotten_q:
            minutes += 1
            l = len(rotten_q)
            for _ in range(l):
                xpos, ypos = rotten_q.popleft()
                for x,y in [(xpos-1,ypos),(xpos+1,ypos),(xpos,ypos-1),(xpos,ypos+1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        rotten_q.append((x,y))
                        cnt_fresh -= 1

                if cnt_fresh == 0:
                    return minutes

        if cnt_fresh : return -1