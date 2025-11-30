class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        preSum = []
        tot, n = 0, 0
        for num in nums:
            tot += num
            preSum.append(tot)
            n += 1
        if tot < p: return -1
        res, rem = n, tot%p 
        hashMap = {}
        hashMap[0] = -1
        if rem == 0: return 0
        for i in range(n):
            curRem = preSum[i]%p
            if nums[i]%p == rem: return 1
            needed = (curRem - rem)%p
            if needed in hashMap:
                res = min(res, i-hashMap[needed])
            hashMap[curRem] = i

        return res if res < n else -1
                