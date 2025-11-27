class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        res = -float("inf")
        preSum = defaultdict(int)
        subSum = [None]*k
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            preSum[i] = curSum
            if i >= k-1:
                idx = (i+1)%k
                if not subSum[idx] == None:
                    appending = subSum[idx] + curSum - preSum[i-k]
                    alone = curSum-preSum[i-k]
                    subSum[idx] = max(appending, alone)
                else:
                    subSum[idx] = curSum - preSum[i-k] if i >= k else curSum
                res = max(res, subSum[idx])
        return res