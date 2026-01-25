class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums_copy = sorted(nums)
        res = nums_copy[-1] - nums_copy[0]
        for i in range(len(nums)-k+1):
            res = min(res, nums_copy[i+k-1] - nums_copy[i])
        return res