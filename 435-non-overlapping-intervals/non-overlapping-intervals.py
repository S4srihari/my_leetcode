class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        for interval in intervals:
            if not res or res[-1][1] <= interval[0]:
                res.append(interval)
            else:
                res[-1][1] = min(res[-1][1], interval[1])
        return len(intervals)-len(res)