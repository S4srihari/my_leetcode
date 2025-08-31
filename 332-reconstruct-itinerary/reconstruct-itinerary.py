class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        for start,dest in tickets:
            adjList[start].append(dest)
        for loc in adjList:
            adjList[loc].sort(reverse = True)
        path = []
        def dfs(loc):
            while adjList[loc]:
                nextLoc = adjList[loc].pop()
                dfs(nextLoc)
            path.append(loc)
            return
            
        dfs("JFK")
        return path[::-1]