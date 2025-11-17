class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        n = len(nums)

        pre = [1]*n
        for i in range(1,n):
            if nums[i] >= nums[i-1]:
                pre[i] = pre[i-1] + 1

        prefix = [1]
        for i in range(1,n):
            prefix.append(pre[i]+prefix[i-1])
        
        
        nex = [n]*(n+1)
        for i in range(n-1,-1,-1):
            if pre[i] == 1:
                nex[i] = i
            else:
                nex[i] = nex[i+1]
        
        print(nex)

        for l,r in queries:
            bre = nex[l]
            if bre > r:
                k = r-l+1
                res.append((k*(k+1)//2))
            else:
                k = bre - l
                val = (k*(k+1)//2)
                val += prefix[r] 
                val -= prefix[bre-1] if bre > 0 else 0  
                res.append(val)
        return res 