class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left,right = 0,0
        for right in range(len(nums)):
            if nums[right] == val:
                continue
            else:
                nums[left] = nums[right]
                left += 1
        return left