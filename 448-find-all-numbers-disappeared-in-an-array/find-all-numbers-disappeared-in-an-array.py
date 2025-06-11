class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #hashset = set(nums)
        ans = []
        #for i in range(1,len(nums)+1):
        #    if i not in hashset:
        #        ans.append(i)
        
        for idx in range(len(nums)):
            temp = abs(nums[idx])-1
            nums[temp] *= -1 if nums[temp] > 0 else 1
        for idx in range(len(nums)):
            if nums[idx] > 0:
                ans.append(idx+1)
        
        return ans

