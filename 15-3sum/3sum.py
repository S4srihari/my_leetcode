class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else :
                    res.append([nums[i],nums[j],nums[k]])
                    while j < n-1 and nums[j] == nums[j+1] :
                        j += 1
                    while k > 1 and nums[k-1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
        return res
                