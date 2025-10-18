class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        if not nums : return 0
        nums.sort()
        nums[0] -= k
        res = 1
        cur = nums[0]
        for i in range(1,len(nums)):
            if nums[i] + k > cur:
                nums[i] = max(cur+1, nums[i]-k)
                res += 1
                cur = nums[i]
        return res
            