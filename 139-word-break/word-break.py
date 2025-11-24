class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        seen = [False]*(n+1)
        seen[0] = True
        for i in range(1,n+1):
            for j in range(i):
                if seen[j] and s[j:i] in wordDict:
                    seen[i] = True
        return seen[n]