class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        temp = 0
        dic = {}
        dic[0] = 1
        for i in range(n):
            temp += nums[i]

            if temp - k in dic:
                ans += dic[temp - k]

            if temp not in dic:
                dic[temp] = 1
            else :
                dic[temp] += 1

        return ans