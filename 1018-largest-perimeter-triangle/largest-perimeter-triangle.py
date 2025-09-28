class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        nums.sort()
        while True:
            if len(nums) < 3: return 0
            a,b,c = nums[-3:]
            if a+b>c:
                return a+b+c
            else:
                nums.pop()
        