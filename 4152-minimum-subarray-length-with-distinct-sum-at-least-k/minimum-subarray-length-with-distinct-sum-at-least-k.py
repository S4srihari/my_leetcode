class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mini = n + 1
        left, right = 0,0
        cache = {}
        cur = 0
        for right in range(n+1):
            while cur >= k:
                cache[nums[left]] -= 1
                if cache[nums[left]] == 0:
                    del cache[nums[left]]
                    cur -= nums[left]
                mini = min(mini, right-left)
                left += 1
            if right == n:
                break
            cache[nums[right]] = cache.get(nums[right], 0) + 1
            if cache[nums[right]] == 1:
                cur += nums[right]
        return mini if mini < n + 1 else -1