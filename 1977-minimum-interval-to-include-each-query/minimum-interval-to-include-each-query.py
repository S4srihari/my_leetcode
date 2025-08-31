class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1]*len(queries)
        heap = []
        queries = sorted([(q,i) for i,q in enumerate(queries)])
        intervals.sort()
        j = 0
        for q,i in queries:
            while j < len(intervals) and intervals[j][0] <= q:
                heapq.heappush(heap,(intervals[j][1]-intervals[j][0]+1,intervals[j][1]))
                j += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[i] = heap[0][0]
        return res
            

