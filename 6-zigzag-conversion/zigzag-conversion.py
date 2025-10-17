class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        res = [[] for _ in range(numRows)]
        i,j = 0,0
        while i<n:
            while i<n and j < numRows-1:
                res[j].append(s[i])
                i += 1
                j += 1
            if i == n: break
            res[j].append(s[i])
            i += 1
            j -= 1
            while i<n and j > 0:
                res[j].append(s[i])
                i += 1
                j -= 1
            if i == n: break
            res[j].append(s[i])
            i += 1
            j += 1
            
        ans = ""
        for i in range(numRows):
            ans += "".join(res[i])
        return ans