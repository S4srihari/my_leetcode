class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        if s < p: return -1
        if s%p == 0: return 0
        n = len(nums)
        preSum = 0
        res, rem = n, s%p
        hashMap = {}
        hashMap[0] = -1
        for i in range(n):
            preSum += nums[i]
            curRem = preSum%p
            needed = (curRem - rem)%p
            if needed in hashMap:
                res = min(res, i-hashMap[needed])
            hashMap[curRem] = i

        return res if res < n else -1
                