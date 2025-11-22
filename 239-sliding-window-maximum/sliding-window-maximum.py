class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque([])
        res = []
        for i, val in enumerate(nums):
            while que and nums[que[-1]] < val:
                que.pop()
            que.append(i)
            while que and que[0] <= i - k:
                que.popleft()
            if i >= k-1:
                res.append(nums[que[0]])
        return res