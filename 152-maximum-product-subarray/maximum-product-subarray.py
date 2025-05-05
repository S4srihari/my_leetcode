class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = nums[0]
        curmax = nums[0]
        curmin = nums[0]
        for num in nums[1:]:
            temp = max(num, num*curmax, num*curmin)
            curmin = min(num, num*curmax, num*curmin)
            curmax = temp
            maxp = max(maxp,curmax)
        return maxp