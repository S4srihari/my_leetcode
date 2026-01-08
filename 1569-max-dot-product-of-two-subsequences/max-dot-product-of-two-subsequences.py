class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """ @lru_cache(None)
        def solve(idx1, idx2, flag):
            if idx1 >= len(nums1)  or idx2 >= len(nums2):
                return 0 if flag else float("-inf")    

            take = solve(idx1 + 1, idx2 +1, 1) + nums1[idx1]*nums2[idx2]
            not_take = max(solve(idx1, idx2+1, flag), solve(idx1+1, idx2, flag))
            return max(take, not_take)

        return solve(0, 0, 0) """

        n, m = len(nums1), len(nums2)
        dp = [[float('-inf')] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                product = nums1[i] * nums2[j]
                if i > 0 and j > 0:
                    current_match = max(product, product + dp[i-1][j-1])
                else:
                    current_match = product
                prev_row = dp[i-1][j] if i > 0 else float('-inf')
                prev_col = dp[i][j-1] if j > 0 else float('-inf')
                
                dp[i][j] = max(current_match, prev_row, prev_col)
                
        return dp[n-1][m-1]