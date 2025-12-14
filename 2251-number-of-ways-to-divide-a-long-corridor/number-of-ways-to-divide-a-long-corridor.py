class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = corridor.count('S')
        if seats%2 == 1 or seats < 2:
            return 0
        elif seats == 2:
            return 1
        cnt = 0
        res = 1
        mod = 10**9 + 7
        prev = -1
        for idx,item in enumerate(corridor):
            if item == 'S':
                cnt += 1
                if cnt%2 == 0:
                    prev = idx
                elif cnt > 2:
                    res *= (idx - prev)
                    res %= mod
        return res