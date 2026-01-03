class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        MOD = 10**9 + 7
        rows = len(grid)
        cols = len(grid[0])
        
        # Compute prefix sums of an array for O(1) range queries
        def get_prefix_sum(arr):
            # P[i] stores sum(arr[0]...arr[i-1])
            P = [0] * (cols + 1)
            for i in range(cols):
                P[i+1] = (P[i] + arr[i]) % MOD
            return P
            
        # Query sum in range [left, right] inclusive
        def query(P, left, right):
            l = max(0, left)
            r = min(cols - 1, right)
            if l > r: return 0
            # Result is P[right+1] - P[left]
            return (P[r+1] - P[l]) % MOD


        dp = [1 if grid[rows-1][c] == '.' else 0 for c in range(cols)]
        
        # Calculate the max column deviation allowed for a Vertical move (upward)
        # We need sqrt(1^2 + dx^2) <= d  =>  dx <= sqrt(d^2 - 1)
        vert_limit = int(math.isqrt(d*d - 1))
        
        for r in range(rows - 1, -1, -1):
            
            # 1. Calculate Total Ways to be at (r, c) ready to move UP
            # This includes:
            #   A. Just arrived vertically at c (dp[c])
            #   B. Arrived vertically at k, then moved horizontally to c
            
            P_dp = get_prefix_sum(dp)
            total_ways = [0] * cols
            
            for c in range(cols):
                if grid[r][c] == '#':
                    total_ways[c] = 0
                    continue
                
                # Get sum of vertical arrivals in range [c-d, c+d]
                # This covers both staying at c (dist 0) and moving from k (dist <= d)
                ways = query(P_dp, c - d, c + d) % MOD
                
                # We don't need to distinguish between staying and moving 
                # for the calculation of the *next* step, because both are valid 
                # states before moving up.
                total_ways[c] = ways
            
            # If we are at the top row, the answer is the sum of all valid paths ending here
            if r == 0:
                return sum(total_ways) % MOD
            
            # 2. Propagate to the row above (r-1)
            # We calculate the vertical arrivals for the next iteration (next_dp)
            # Source: total_ways at row r
            # Limit: vert_limit (calculated earlier)
            
            P_total = get_prefix_sum(total_ways)
            next_dp = [0] * cols
            
            for c in range(cols):
                if grid[r-1][c] == '#':
                    next_dp[c] = 0
                else:
                    # Valid sources are within [c - vert_limit, c + vert_limit]
                    next_dp[c] = query(P_total, c - vert_limit, c + vert_limit)
            
            dp = next_dp
            
        return 0