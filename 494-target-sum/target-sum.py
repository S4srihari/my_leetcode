class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        if s%2 != target%2 : return 0
        new_target = (s+target)//2
        if new_target < 0:
            return 0
        prev = [0]*(new_target+1)
        prev[0] = 1 
        if nums[0] == 0: prev[0] = 2
        elif nums[0] <= new_target : prev[nums[0]] = 1

        for idx in range(1,n):
            for T in range(new_target,-1,-1):
                not_take = prev[T]
                take = 0
                if nums[idx] <= T :
                    take = prev[T-nums[idx]]
                prev[T] = not_take + take
        
        return prev[new_target]