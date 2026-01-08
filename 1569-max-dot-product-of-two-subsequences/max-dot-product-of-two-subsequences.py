class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def solve(idx1, idx2, buf, flag):
            if idx1 >= len(nums1)  or idx2 >= len(nums2):
                return 0 if flag else float("-inf")
        
            if buf is None:
                take = solve(idx1, idx2, nums1[idx1], flag)
                not_take = solve(idx1 + 1, idx2, buf, flag)
                return max(take, not_take)
                
            else:
                take = solve(idx1 + 1, idx2 +1, None, 1) + buf*nums2[idx2]
                not_take = solve(idx1, idx2+1, buf, flag)
                return max(take, not_take)


        return solve(0, 0, None, 0)