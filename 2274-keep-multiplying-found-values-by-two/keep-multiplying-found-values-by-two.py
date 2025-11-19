class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)
        num = original
        while num in s:
            num *= 2
        return num