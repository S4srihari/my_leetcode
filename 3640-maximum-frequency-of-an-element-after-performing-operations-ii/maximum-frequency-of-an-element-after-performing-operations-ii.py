class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        c = Counter(nums)
        nums.sort()
        res = 0
        for j in c.keys():
            for i in (j, j+k, j-k):
                left = bisect_left(nums, i-k)
                right = bisect_right(nums, i+k)
                cur = min(right-left, c[i] + numOperations)
                res = max(res, cur)
        return res