class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10**9 + 7
        lines = defaultdict(set)
        for x,y in points:
            lines[y].add(x)
        cntlines = []
        for line in lines:
            cords = len(lines[line]) 
            if cords > 1:
                cntlines.append(cords)
        if len(cntlines) <= 1:
            return 0
        res = 0
        cntlines = [(i*(i-1))//2 for i in cntlines]
        tot = sum(cntlines)
        for cnt in cntlines:
            res += (tot-cnt)*cnt
        res = res//2
        return res%mod