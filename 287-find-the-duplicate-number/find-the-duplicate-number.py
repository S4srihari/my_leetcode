class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """nums.sort()
        for idx in range(1,len(nums)):
            if nums[idx] == nums[idx-1]:
                return nums[idx]"""

        """n = len(nums)
        k = [0]*n
        for num in nums:
            if k[num] == 1:
                return num
            k[num] = 1"""
        
        # Floyd's Tortoise and Hare Algorithm
        slow,fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow