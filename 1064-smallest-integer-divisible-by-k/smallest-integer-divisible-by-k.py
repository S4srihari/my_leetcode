class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0 or k%5 == 0: return -1
        res = 1
        n = 1
        while (n%k != 0) and res <= k+1:
            res += 1
            n = n*10 + 1 
        return res