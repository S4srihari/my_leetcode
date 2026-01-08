class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def solve(idx1, idx2, flag):
            if idx1 >= len(nums1)  or idx2 >= len(nums2):
                return 0 if flag else float("-inf")
                
            take = solve(idx1 + 1, idx2 +1, 1) + nums1[idx1]*nums2[idx2]
            not_take = max(solve(idx1, idx2+1, flag), solve(idx1+1, idx2, flag))
            return max(take, not_take)


        return solve(0, 0, 0)