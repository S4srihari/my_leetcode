class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31):
            res <<= 1
            n >>= 1
            if n & 1:
                res += 1
        return res