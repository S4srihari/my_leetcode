class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        if sum(nums)%2 == 1:
            return 0
        else:
            return len(nums)-1