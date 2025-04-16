class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0
        dic = {}
        l = 0
        for i in range(n):
            if nums[i] not in dic:
               dic[nums[i]] = 0
            k -= dic[nums[i]]
            dic[nums[i]] += 1
            while k <= 0 :
                dic[nums[l]] -= 1
                k += dic[nums[l]]
                l += 1
            ret += l
        return ret