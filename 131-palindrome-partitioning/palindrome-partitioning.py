class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        is_pal = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i+1][j-1]):
                    is_pal[i][j] = True

        def backtrack(idx,cur):
            if idx == n:
                res.append(cur[:])
            for i in range(idx,n):
                if is_pal[idx][i]:
                    cur.append(s[idx:i+1])
                    backtrack(i+1,cur)
                    cur.pop()
        backtrack(0,[])
        return res