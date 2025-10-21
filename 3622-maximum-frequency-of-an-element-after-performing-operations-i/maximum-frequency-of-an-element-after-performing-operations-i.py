class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        c = Counter(nums)
        nums.sort()
        res = 0
        for i in range(nums[0], nums[-1]+1):
            left = bisect_left(nums, i-k)
            right = bisect_right(nums, i+k)
            cur = c[i] + min(right-left-c[i], numOperations)
            res = max(res, cur)
        return res