class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[left] <= nums[mid]:  # No pivot on left side
                if nums[mid] <= nums[right]: # No pivot on both sides
                    return nums[left]
                else :
                    left = mid + 1
            else :
                right = mid
        return nums[left]