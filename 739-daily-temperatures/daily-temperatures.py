class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i in range(n-1,-1,-1):
            if i == n-1:
                stack.append((temperatures[i],1))
            cnt = 1
            while stack and stack[-1][0] <= temperatures[i]:
                cnt += stack[-1][1]
                stack.pop()
            if stack : 
                res[i] = cnt 
            stack.append((temperatures[i],cnt))
        return res