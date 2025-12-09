class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        cnt, mod = 0, 10**9 + 7
        total = {}
        for i in range(len(nums)):
            total[nums[i]] = total.get(nums[i], 0)  + 1
        cur = {}
        for i in range(len(nums)):
            if nums[i] == 0: continue
            if nums[i]*2 in total and nums[i]*2 in cur:
                cnt += cur[nums[i]*2] * (total[nums[i]*2] - cur[nums[i]*2])
                cnt %= mod
            cur[nums[i]] = cur.get(nums[i], 0) + 1
        zeroes = total[0] if 0 in total else 0
        cnt += zeroes*(zeroes-1)*(zeroes-2)//6
        cnt %= mod
        return cnt