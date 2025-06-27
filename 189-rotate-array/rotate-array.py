class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        temp = nums[-k:] + nums[:-k]
        for idx in range(len(nums)):
            nums[idx] = temp[idx]