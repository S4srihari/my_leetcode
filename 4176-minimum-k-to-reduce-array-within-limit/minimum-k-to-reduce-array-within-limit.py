class Solution:
    def minimumK(self, nums: List[int]) -> int:
        left, right = 1, sum(nums)+1
        ans = right

        def possible(val):
            tot = 0
            for i in nums:
                tot += (i+val-1)//val
            return tot <= val**2

        while left <= right:
            mid = left + (right-left)//2

            if possible(mid):
                right = mid-1
                ans = mid
            else:
                left = mid + 1
        
        return ans