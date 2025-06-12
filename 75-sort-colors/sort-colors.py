class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """c = Counter(nums)
        for i in range(len(nums)):
            if i < c[0]:
                nums[i] = 0
            elif i < c[0] + c[1]:
                nums[i] = 1
            else :
                nums[i] = 2"""
        
        n = len(nums)
        left, right,i = 0,n-1,0
        while i < n:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums[left],nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            else:
                if i < right:
                    nums[right],nums[i] = nums[i],nums[right]
                    right -= 1
                else :
                    break