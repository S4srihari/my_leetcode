class Solution:
    def subset_sum(self,target, nums):
        n = len(nums)
        ways = [[False]*(target+1) for _ in range(n)]
        for _ in range(n):
            ways[_][0] = True
        if nums[0] <= target : ways[0][nums[0]] = True
        
        for idx in range(n):
            for T in range(1,target+1):
                not_take = ways[idx-1][T]
                take = False
                if nums[idx] <= T:
                    take = ways[idx-1][T-nums[idx]]
                ways[idx][T] = take or not_take
        return ways[n-1][T] 

        """prev = [True] + [0]*(target)
        if arr[0] <= target:
            prev[arr[0]] = True 
        for idx in range(1,len(arr)):
            cur =  [True] + [0]*(target)
            for t in range(target+1):
                not_take = prev[t]
                take = False
                if t >= arr[idx]:
                    take = prev[t-arr[idx]]
                cur[t] = take or not_take 
                if cur[target] == True:
                    return True
            prev = cur

        return prev[target] is True"""

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2 == 1:
            return False
        else:
            return self.subset_sum(total_sum//2,nums)
            