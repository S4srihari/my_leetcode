class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = [(temperatures[n-1],1)]
        for i in range(n-2,-1,-1):
            cnt = 1
            while stack and stack[-1][0] <= temperatures[i]:
                cnt += stack[-1][1]
                stack.pop()
            if stack : 
                res[i] = cnt 
            stack.append((temperatures[i],cnt))
        return res
