class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2 == 1: return False
        half = s//2
        dp = set()
        dp.add(0)
        for num in nums:
            temp = set()
            for p in dp:
                if num + p == half:
                    return True
                temp.add(num+p)
                temp.add(p)
            dp = temp
        return False


        """dp = [True] + [False]*half
        for num in nums:
            for i in range(half, num-1,-1):
                dp[i] = dp[i] or dp[i-num]
            if dp[-1] :return True

        return False """
