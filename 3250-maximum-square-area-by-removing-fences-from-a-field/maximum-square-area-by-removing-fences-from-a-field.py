class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        mod = 10**9 + 7
        if m == n:
            return (m-1)*(n-1) % mod
        heights = set()
        hors = [i for i in hFences] + [1,m]
        hors.sort()
        vers = [i for i in vFences] + [1,n]
        vers.sort()
        res = -1
        for i in range(len(hors)):
            for j in range(i+1,len(hors)):
                heights.add(abs(hors[i]-hors[j]))
        for i in range(len(vers)):
            for j in range(i+1,len(vers)):
                width = abs(vers[i]-vers[j])
                if width in heights:
                    res = max(res, width**2)
        
        return res%mod if res > 0 else -1

