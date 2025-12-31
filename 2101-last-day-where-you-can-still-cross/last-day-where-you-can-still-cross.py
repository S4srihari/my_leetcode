class Solution:
    def can_traverse(self, idx, row, col, cells):
        grid = [[0]*col for _ in range(row)]
        for i in range(idx):
            r,c = cells[i]
            grid[r-1][c-1] = 1
        
        vis = set()
        route = deque([])
        for j in range(col):
            if grid[0][j] == 0:
                route.append((0,j))
                vis.add((0,j))
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        while route:
            r,c = route.popleft()
            if r == row - 1:
                return True
            for dr,dc in dirs:
                if 0 <= r+dr < row and 0 <= c+dc <col and (r+dr,c+dc) not in vis and grid[r+dr][c+dc] == 0:
                    vis.add((r+dr,c+dc))
                    route.append((r+dr,c+dc))
        return False
        
        
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        ans = 0
        left,right = 0, len(cells)-1
        while left <= right:
            mid = left + (right - left)//2
            if self.can_traverse(mid, row, col, cells):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans 