class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        pre_sum = []
        sub = 0
        for i in range(n):
            sub += nums[i]
            pre_sum.append(sub)
        p_hash = {}
        p_hash[0] = 1
        for i in range(n):
            if pre_sum[i] - k in p_hash:
                ans += p_hash[pre_sum[i] - k]

            if pre_sum[i] not in p_hash:
                p_hash[pre_sum[i]] = 1
            else :
                p_hash[pre_sum[i]] += 1
        return ans