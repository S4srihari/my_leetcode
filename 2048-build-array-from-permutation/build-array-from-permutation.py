class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """res = [-1]*len(nums)
        for i in range(len(nums)):
            res[i] = nums[nums[i]]
        return res"""

        #without extra space
        
        for i in range(len(nums)):
            nums[i] += 1000 *(nums[nums[i]]%1000)  
        print(nums)
        for i in range(len(nums)):
            nums[i] //= 1000
        return nums