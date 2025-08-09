class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """cnt = 0
        while n:
            cnt += n & 1
            if cnt > 1:
                return False
            n = n>>1
        return cnt == 1"""

        return n > 0 and not(n & (n-1))