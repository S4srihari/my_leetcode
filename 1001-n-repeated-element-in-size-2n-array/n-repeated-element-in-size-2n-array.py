class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return 0

        # Tc = O(n)
        # Sc = O(n)