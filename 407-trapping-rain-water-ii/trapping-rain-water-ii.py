class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap: return 0
        m = len(heightMap)
        n = len(heightMap[0])
        water = 0
        que = deque([])
        heap = []
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            if i == 0 or i == m-1:
                for j in range(n):
                    heap.append((heightMap[i][j], i, j))
            else:
                heap.append((heightMap[i][0], i, 0))
                heap.append((heightMap[i][n-1], i, n-1))
        heapq.heapify(heap)
        dirs = [0,1,0,-1,0]
        while heap:
            height,i,j = heapq.heappop(heap)
            que.append((height,i,j))
            while que:
                height,x,y = que.popleft()
                visited[x][y] = True
                for d in range(4):
                    if x+dirs[d]>=0 and x+dirs[d]<m and y+dirs[d+1]>=0 and y+dirs[d+1]<n and not visited[x+dirs[d]][y+dirs[d+1]]:
                        if heightMap[x+dirs[d]][y+dirs[d+1]] < height:
                            water += height - heightMap[x+dirs[d]][y+dirs[d+1]] 
                            heightMap[x+dirs[d]][y+dirs[d+1]] = height
                            que.append((height,x+dirs[d],y+dirs[d+1]))
                            visited[x+dirs[d]][y+dirs[d+1]] = True
                        else:
                            heapq.heappush(heap, (heightMap[x+dirs[d]][y+dirs[d+1]], x+dirs[d], y+dirs[d+1]))
        return water