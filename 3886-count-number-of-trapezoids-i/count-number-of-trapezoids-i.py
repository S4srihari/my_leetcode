class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10**9 + 7
        lines = defaultdict(int)
        for x,y in points:
            lines[y] += 1
        tot = 0
        sq_sum = 0
        for cnt in lines.values():
            if cnt>1: 
                sides = (cnt*(cnt-1))//2
                tot += sides
                sq_sum += sides*sides
        res = tot*tot - sq_sum
        res = res//2
        return res%mod