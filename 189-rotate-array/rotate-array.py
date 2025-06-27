class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        for _ in range(k):
            last_ele = nums.pop()
            nums.insert(0,last_ele)
        