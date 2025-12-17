class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if int(nums[i]) > 0 and int(nums[i]) <= n:
                nums[int(nums[i])-1] = str(nums[int(nums[i])-1])
        
        res = 1
        for i in range(n):
            if type(nums[i]) is str:
                res += 1
            else:
                break
        return res