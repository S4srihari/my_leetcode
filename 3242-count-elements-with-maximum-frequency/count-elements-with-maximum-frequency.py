class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        maxF, res = 0,0
        for num, freq in c.items():
            if freq > maxF:
                maxF = freq
                res = maxF
            elif freq == maxF:
                res += maxF
        return res