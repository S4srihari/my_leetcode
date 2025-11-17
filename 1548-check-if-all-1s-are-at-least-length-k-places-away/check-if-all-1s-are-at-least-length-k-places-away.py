class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -k-1
        for i in range(len(nums)):
            if nums[i] == 1 and i-prev <= k:
                return False
            elif nums[i] == 1:
                prev = i
        return True