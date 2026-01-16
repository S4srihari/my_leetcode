class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        mod = 10**9 + 7
        if m == n:
            return (m-1)*(n-1) % mod
        hor_dis = set()
        ver_dis = set()
        hors = [i for i in hFences] + [1,m]
        vers = [i for i in vFences] + [1,n]
        for i in hors:
            for j in hors:
                hor_dis.add(abs(i-j))
        for i in vers:
            for j in vers:
                ver_dis.add(abs(i-j))
        res = -1
        for x in hor_dis:
            if x !=0 and x in ver_dis:
                res = max(res, x**2)
        return res%mod if res > 0 else res

