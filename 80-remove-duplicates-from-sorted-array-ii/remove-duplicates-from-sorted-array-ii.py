class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        cnt = 1
        for idx in range(1,len(nums)):
            if nums[idx] != nums[slow]:
                slow += 1
                nums[slow] = nums[idx]
                cnt = 1
            else:
                cnt += 1
                if cnt <= 2:
                    slow += 1
                    nums[slow] = nums[idx]
        return slow+1