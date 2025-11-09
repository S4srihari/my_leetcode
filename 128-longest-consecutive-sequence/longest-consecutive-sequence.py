class unionFind:
    def __init__(self):
        self.parent = {}

    def find(self,num):
        if self.parent[num] != num:
            self.parent[num] = self.find(self.parent[num])
        return self.parent[num]
    
    def union(self,num1, num2):
        self.parent[num2] = num1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visEle = set()
        uf = unionFind()
        for num in nums:
            if num+1 in visEle:
                uf.union(num,num+1)
            if num-1 in visEle:
                uf.union(num-1,num)
            else:
                uf.union(num,num)
            visEle.add(num)
        
        cnt =  defaultdict(int)
        res = 0
        for num in visEle:
            grp = uf.find(num)
            cnt[grp] += 1
            res = max(res,cnt[grp])
        return res