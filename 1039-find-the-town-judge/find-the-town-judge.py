class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0]*(n+1)
        trust_count = [0]*(n+1)
        for per,tru in trust:
            trusts[per] += 1
            trust_count[tru] += 1
        for per in range(1,n+1):
            if trust_count[per] == n-1 and trusts[per] == 0: 
                return per
        return -1 