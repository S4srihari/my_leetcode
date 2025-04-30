class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """value = 0
        n = len(nums) 
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    value = max(value, (nums[i] - nums[j]) * nums[k])
        return value"""
        high, diff, ans = 0,0,0
        for num in nums:
            if diff*num > ans:
                ans = diff*num
            if high - num > diff:
                diff = high - num
            if num > high:
                high = num
        return ans