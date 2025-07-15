class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n:
            if n & 1:
                ones += 1
            n = n >> 1
        return ones