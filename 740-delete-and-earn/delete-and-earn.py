class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)
        l = sorted([(k, k*v) for k,v in c.items()])
        if len(l) < 2:
            return l[0][1]
        prev, prev2 = l[0][1],0
        for idx in range(1,len(l)):
            if l[idx][0] - l[idx-1][0] > 1:
                cur = max(prev,prev2) + l[idx][1]
            else :
                cur = max(prev, prev2 + l[idx][1])
            prev2 = prev
            prev = cur
        return prev