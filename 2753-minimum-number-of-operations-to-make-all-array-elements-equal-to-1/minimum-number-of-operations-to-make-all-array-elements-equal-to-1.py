class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        gc = 0
        ones = 0
        for num in nums:
            if num == 1: 
                ones += 1
            gc = gcd(gc,num)

        if ones: return n-ones
        elif gc > 1: return -1

        mini = float("inf")
        for i  in range(n-1):
            gc = 0
            for j in range(i,n):
                gc = gcd(gc,nums[j])
                if gc == 1:
                    mini = min(mini,j-i+1)
                    break
                    
        return mini-1 + n-1 if mini != float("inf") else -1