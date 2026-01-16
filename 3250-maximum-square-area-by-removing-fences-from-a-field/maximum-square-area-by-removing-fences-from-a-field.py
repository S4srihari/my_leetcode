class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        mod = 10**9 + 7
        if m == n:
            return (m-1)*(n-1) % mod
        hor_dis = set()
        ver_dis = set()
        hors = [i for i in hFences] + [1,m]
        hors.sort()
        vers = [i for i in vFences] + [1,n]
        vers.sort()
        for i in range(len(hors)):
            for j in range(i+1,len(hors)):
                hor_dis.add(abs(hors[i]-hors[j]))
        for i in range(len(vers)):
            for j in range(i+1,len(vers)):
                ver_dis.add(abs(vers[i]-vers[j]))
        res = -1
        for x in hor_dis:
            if x !=0 and x in ver_dis:
                res = max(res, (x**2))
        return res%mod if res > 0 else -1

