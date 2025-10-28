class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        tot = sum(nums)
        cur = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0 and cur == tot-cur:
                res += 2
            elif nums[i] == 0 and abs(cur-(tot-cur)) <= 1:
                res += 1
            cur += nums[i]
        return res