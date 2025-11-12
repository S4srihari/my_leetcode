class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = set(nums)
        eve = 0
        odd = 0
        for num in s:
            if num%2 : odd += 1
            else : eve += 1

        if odd == 0: return -1
        elif odd == 1 and eve == 0: 
            return -1 if nums[0] != 1 else 0

        ones = nums.count(1)
        if ones:
            return len(nums)-ones

        def findgcd(i,j):
            res = nums[i]
            for idx in range(i+1,j+1):
                res = math.gcd(res,nums[idx])
            return res

        n = len(nums)
        mini = float("inf")
        for i  in range(n-1):
            for j in range(i+1,n):
                if findgcd(i,j) == 1:
                    mini = min(mini,j-i+1)
        return mini-1 + n-1 if mini != float("inf") else -1