class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        left , right = 0,len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target and (mid == 0 or nums[mid-1] < nums[mid]):
                res[0] = mid 
                break
            elif nums[mid] < target:
                left = mid + 1
            else :
                right = mid - 1

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target and (mid == len(nums) -1 or nums[mid+1] > nums[mid]):
                res[1] = mid 
                break
            elif nums[mid] > target:
                right = mid - 1
            else :
                left = mid + 1
        
        return res