class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n_hash = {0:-1}
        ans = 0
        cursum = 0
        for idx in range(len(nums)):
            cursum += 1 if nums[idx] == 1 else -1
            if cursum not in n_hash:
                n_hash[cursum] = idx
            ans = max(ans, idx -  n_hash[cursum])

        return ans