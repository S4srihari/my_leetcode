class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        st = deque([])
        res = []
        for i in range(len(nums)):
            while st and st[-1][0] < nums[i]:
                st.pop()
            st.append((nums[i], i))
            while st and st[0][1] <= i - k:
                st.popleft()
            if i >= k-1:
                res.append(st[0][0])
        return res