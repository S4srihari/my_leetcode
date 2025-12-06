class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        prefix_dp = [0] * (n + 2)
        prefix_dp[1] = 1  
        min_q = deque() 
        max_q = deque()
        left = 0
        for right in range(n):
            while max_q and nums[max_q[-1]] <= nums[right]:
                max_q.pop()
            max_q.append(right)

            while min_q and nums[min_q[-1]] >= nums[right]:
                min_q.pop()
            min_q.append(right)

            while nums[max_q[0]] - nums[min_q[0]] > k:
                left += 1
                if max_q[0] < left:
                    max_q.popleft()
                if min_q[0] < left:
                    min_q.popleft()
            count = (prefix_dp[right + 1] - prefix_dp[left]) % MOD
            dp[right + 1] = count
            prefix_dp[right + 2] = (prefix_dp[right + 1] + dp[right + 1]) % MOD
        return dp[n]