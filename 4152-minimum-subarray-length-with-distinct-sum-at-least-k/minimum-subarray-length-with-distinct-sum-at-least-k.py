class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        # Brute Force
        # Tc = O(n**2) 
        # Using Sliding Window and HashMap

        n = len(nums)
        res = n+1
        cache = {}
        curSum = 0
        left = 0
        for right in range(n+1):
            while curSum >= k:
                cache[nums[left]] -= 1
                if cache[nums[left]] == 0:
                    curSum -= nums[left]
                    del cache[nums[left]]
                res = min(res, right-left)
                left += 1
            if right == n:
                break
            cache[nums[right]] = cache.get(nums[right], 0) + 1
            if cache[nums[right]] == 1:
                curSum += nums[right]
        return res if res <= n else -1