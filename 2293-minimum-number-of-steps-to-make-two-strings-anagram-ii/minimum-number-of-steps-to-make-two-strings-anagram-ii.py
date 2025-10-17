class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """arr = [0]*26
        for c in s:
            arr[ord(c)-ord('a')] += 1
        for c in t:
            arr[ord(c)-ord('a')] -= 1
        res = 0
        for i in range(26):
            res += abs(arr[i])
        return res"""

        a = list(set(s) | set(t)) 
        b = {i:s.count(i) for i in a}
        c = {i:t.count(i) for i in a}
        n = 0
        for i in a:
            n += min(b[i],c[i])
        return len(s)+len(t)-2*n