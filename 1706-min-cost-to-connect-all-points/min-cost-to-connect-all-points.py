class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False]*n
        heap = [(0,0)]
        dist = [float("inf")]*n
        dist[0] = 0
        res = 0

        while heap:
            wt, node = heapq.heappop(heap)
            if visited[node] == True:
                continue
            visited[node] = True
            res += wt
            for i in range(n):
                if visited[i]:
                    continue
                curDist = abs(points[i][0]-points[node][0]) + abs(points[i][1]-points[node][1])
                dist[i] = min(dist[i],curDist)
                heapq.heappush(heap,(dist[i],i))
        return res