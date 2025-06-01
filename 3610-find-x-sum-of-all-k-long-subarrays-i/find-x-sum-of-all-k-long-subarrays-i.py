class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        dic = {}
        for i in range(k):
            dic[nums[i]] = dic.get(nums[i],0) + 1
        res = []
        n = len(nums)
        for i in range(k,n+1):
            d = sorted(dic.items(), key = lambda x: (x[1],x[0]), reverse = True)
            res.append(sum([k*v for k,v in d[:x]]))
            if i == n:
                return res
            dic[nums[i]] = dic.get(nums[i],0) + 1
            dic[nums[i-k]] -= 1