class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0: return -1
        elif k%5 == 0: return -1
        seen = set()
        res = 1
        n = 1
        while (n%k != 0) and n not in seen:
            res += 1
            seen.add(n)
            n = n*10 + 1 
        if n in seen:
            return -1
        else :
            return res