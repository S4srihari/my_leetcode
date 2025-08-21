class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def palindrome(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i,j = i+1,j-1
            return True

        def backtrack(idx,cur):
            if idx == n:
                res.append(cur[:])
            for i in range(idx,n):
                if palindrome(idx,i):
                    cur.append(s[idx:i+1])
                    backtrack(i+1,cur)
                    cur.pop()
        backtrack(0,[])
        return res