class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if int(str(nums[j+1])+str(nums[j])) > int(str(nums[j])+str(nums[j+1])):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        if any(nums):
            return "".join([str(i) for i in nums])
        else:
            return "0"