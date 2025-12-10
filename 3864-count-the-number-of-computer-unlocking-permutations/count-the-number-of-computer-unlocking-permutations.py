class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        cnt = 1
        mod = 10**9 + 7
        for i in range(1,len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
            cnt *= i
            cnt %= mod
        return cnt