class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10**9 + 7
        lines = defaultdict(int)
        for x,y in points:
            lines[y] += 1
        cntlines = []
        tot = 0
        for line in lines:
            cords = lines[line]
            sides = (cords*(cords-1))//2
            tot += sides
            cntlines.append(sides)
        res = 0
        for cnt in cntlines:
            res += (tot-cnt)*cnt
        res = res//2
        return res%mod