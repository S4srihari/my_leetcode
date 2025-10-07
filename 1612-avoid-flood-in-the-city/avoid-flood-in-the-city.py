class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        nextRain = defaultdict(list)

        for i in range(n-1, -1, -1):
            lake = rains[i]
            if lake:
                nextRain[lake].append(i)

        full = set()
        heap = []  
        ans = []

        for i, lake in enumerate(rains):
            if lake:
                if lake in full:
                    return [] 
                full.add(lake)
                nextRain[lake].pop()
                
                if nextRain[lake]:
                    heapq.heappush(heap, (nextRain[lake][-1], lake))
                ans.append(-1)
            else:
                if heap:
                    _, dryLake = heapq.heappop(heap)
                    full.remove(dryLake)
                    ans.append(dryLake)
                else:
                    ans.append(1)
        return ans