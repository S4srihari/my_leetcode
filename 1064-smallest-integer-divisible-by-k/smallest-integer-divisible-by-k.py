class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0 or k%5 == 0: return -1
        seen = set()
        res = 1
        n = 1
        while (n%k != 0) and n not in seen and res <= k+1:
            res += 1
            seen.add(n)
            n = n*10 + 1 
        if n in seen:
            return -1
        else :
            return res