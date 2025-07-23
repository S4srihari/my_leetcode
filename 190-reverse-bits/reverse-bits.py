class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = res << 1
            res += 1 if n&1 else 0
            n = n >> 1
        return res 