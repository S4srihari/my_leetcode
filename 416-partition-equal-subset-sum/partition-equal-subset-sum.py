class Solution:
    def subset_sum(self,idx, target, arr,dp):
        if target == 0: return True
        elif idx == 0: return arr[0] == target
        elif dp[idx][target] != -1 :
            return dp[idx][target]
        else :
            not_take = self.subset_sum(idx-1,target,arr,dp)
            take = False
            if target-arr[idx] >= 0:
                take = self.subset_sum(idx-1,target-arr[idx],arr,dp)
            dp[idx][target] = take or not_take 
        return dp[idx][target]
        
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2 == 1:
            return False
        else:
            dp = [[-1]*((total_sum//2)+1) for _ in range(len(nums))]
            return self.subset_sum(len(nums)-1,total_sum//2, nums,dp)