class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n_hash = defaultdict(list)
        ans = 0
        cursum = 0
        for idx in range(len(nums)):
            cursum += 1 if nums[idx] == 1 else -1
            n_hash[cursum].append(idx)
            if cursum == 0:
                ans = max(ans,idx+1)
            elif len(n_hash[cursum]) >= 2:
                ans = max(ans,n_hash[cursum][-1] - n_hash[cursum][0])

        return ans