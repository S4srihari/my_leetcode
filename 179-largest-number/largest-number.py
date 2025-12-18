class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = [str(i) for i in nums]
        for i in range(n):
            for j in range(n-i-1):
                if nums[j+1]+nums[j] > nums[j]+nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        if any([int(i) for i in nums]):
            return "".join(nums)
        else:
            return "0"