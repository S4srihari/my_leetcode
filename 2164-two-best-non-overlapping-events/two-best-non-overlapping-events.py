class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[1])
        cache = {}
        end_times = []
        max_seen =  0
        res = 0
        for event in events:
            if end_times:
                idx = bisect_left(end_times, event[0])
                if idx > 0:
                    res = max(res, cache[end_times[idx-1]]+event[2])
            max_seen = max(max_seen, event[2])
            end_times.append(event[1])
            cache[event[1]] = max_seen
        return max(res,max_seen)