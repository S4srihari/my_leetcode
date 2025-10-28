class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        tot = sum(nums)
        cur = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if cur == tot-cur:
                    res += 2
                elif abs(cur-(tot-cur)) <= 1:
                    res += 1
            else:
                cur += nums[i]
        return res