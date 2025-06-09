class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """nums.sort()
        for idx in range(1,len(nums)):
            if nums[idx] == nums[idx-1]:
                return nums[idx]"""
        n = len(nums)
        k = [0]*n
        for num in nums:
            if k[num] == 1:
                return num
            k[num] = 1
                