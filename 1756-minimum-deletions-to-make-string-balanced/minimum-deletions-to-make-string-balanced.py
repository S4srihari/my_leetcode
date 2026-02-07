class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        prev_b = []
        post_a = [0]*n
        cur_b = 0
        for i in range(n):
            prev_b.append(cur_b)
            if s[i] == 'b':
                cur_b += 1
        cur_a = 0
        for i in range(n-1,-1,-1):
            post_a[i] = cur_a
            if s[i] == 'a':
                cur_a += 1
        
        res = n
        for i in range(n):
            res = min(res, prev_b[i]+post_a[i])
        return res