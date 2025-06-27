class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Using Extra Space
        """k %= len(nums)
        temp = nums[-k:] + nums[:-k]
        for idx in range(len(nums)):
            nums[idx] = temp[idx]"""
        n = len(nums)
        k %= n
        if k == 0: return
        nums[-k:] = nums[-k:][::-1]
        nums[:n-k] = nums[:n-k][::-1]
        nums[:] = nums[:][::-1]