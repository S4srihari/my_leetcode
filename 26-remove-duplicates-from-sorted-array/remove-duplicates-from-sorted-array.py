class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast,slow = 0,0
        while fast < len(nums):
            if fast == 0 or nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow