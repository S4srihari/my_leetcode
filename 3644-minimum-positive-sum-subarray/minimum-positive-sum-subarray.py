class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')
        for win in range(l,r+1):
            win_sum = 0
            for idx in range(n):
                win_sum += nums[idx]
                if idx >= win:
                    win_sum -= nums[idx-win]
                if idx >= win-1 and win_sum > 0:
                    ans = min(ans, win_sum)

        return -1 if ans == float('inf') else ans 