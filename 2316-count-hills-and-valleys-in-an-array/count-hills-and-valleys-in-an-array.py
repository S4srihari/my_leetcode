class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hills,valleys = 0,0
        n = len(nums)
        for i in range(1,n-1):
            j = i-1
            while i < n-2 and nums[i] == nums[i+1]:
                i += 1
            if nums[i] > nums[j] and nums[i] > nums[i+1]:
                hills +=1
            if nums[i] < nums[i+1] and nums[i] < nums[j]:
                valleys += 1
        return hills + valleys
             