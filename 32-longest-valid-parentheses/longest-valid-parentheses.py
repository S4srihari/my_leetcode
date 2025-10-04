class Solution:
    def longestValidParentheses(self, s: str) -> int:
        op = 0
        cl = 0
        ans = 0
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                op += 1
            else:
                cl += 1
            if op == cl:
                ans = max(ans, op)
            if cl > op:
                op = 0
                cl = 0
        op = 0
        cl = 0
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            if c == ")":
                op += 1
            else:
                cl += 1
            if op == cl:
                ans = max(ans, op)
            if cl > op:
                op = 0
                cl = 0
        return ans*2