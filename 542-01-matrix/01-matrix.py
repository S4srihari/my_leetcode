class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat : return []
        m,n = len(mat), len(mat[0])
        ans = [[float('inf')]*n for _ in range(m)]
        q = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i,j))
                    visited.add((i,j))
        while q:
            x,y = q.popleft()
            for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= i < m and 0 <= j < n and (i,j) not in visited:
                    ans[i][j] = min(ans[i][j], 1+ans[x][y])
                    q.append((i,j))
                    visited.add((i,j))
        return ans