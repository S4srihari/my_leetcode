class Solution:
    def subset_sum(self,target, arr):
        prev = [True] + [0]*(target)
        if arr[0] > target: return False
        prev[arr[0]] = True 
        for idx in range(1,len(arr)):
            cur =  [True] + [0]*(target)
            for t in range(target+1):
                not_take = prev[t]
                take = False
                if t >= arr[idx]:
                    take = prev[t-arr[idx]]
                cur[t] = take or not_take 
            prev = cur

        return prev[target] is True

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2 == 1:
            return False
        else:
            return self.subset_sum(total_sum//2,nums)
            