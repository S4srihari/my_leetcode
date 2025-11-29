class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        return s%k