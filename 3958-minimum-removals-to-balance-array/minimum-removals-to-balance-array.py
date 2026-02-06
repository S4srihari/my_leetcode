class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        arr = [i  for i in nums]
        arr.sort()
        n = len(arr)
        res = n-1
        for i in range(n):
            idx = bisect_right(arr, arr[i]*k)
            removals = n - (idx-i)
            res = min(res,removals)
        return res