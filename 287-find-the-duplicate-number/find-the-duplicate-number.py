class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for idx in range(1,len(nums)):
            if nums[idx] == nums[idx-1]:
                return nums[idx]