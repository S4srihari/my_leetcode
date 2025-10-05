class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl= set(), set(),
        pq, aq = deque([]), deque([])
        for i in range(m):
            pac.add((i,0))
            pq.append((i,0))
            
            atl.add((i,n-1))
            aq.append((i,n-1))
            
        for j in range(n):
            pac.add((0,j))
            pq.append((0,j))
            
            atl.add((m-1,j))
            aq.append((m-1,j))
            
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while pq:
            x,y = pq.popleft()
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if nx>=0 and nx<m and ny>=0 and ny<n and (nx,ny) not in pac and heights[nx][ny] >= heights[x][y]:
                    pac.add((nx,ny))
                    pq.append((nx,ny))
        while aq:
            x,y = aq.popleft()
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if nx>=0 and nx<m and ny>=0 and ny<n and (nx,ny) not in atl and heights[nx][ny] >= heights[x][y]:
                    atl.add((nx,ny))
                    aq.append((nx,ny))
        res = []
        for loc in pac:
            if loc in atl:
                res.append(loc)
        return res          