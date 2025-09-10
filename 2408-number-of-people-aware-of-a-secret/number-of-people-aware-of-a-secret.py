class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        if forget <= delay: return 1 if forget > n else 0
        know = deque([(1,1)])
        share = deque([])
        knowCnt, shareCnt = 1,0
        for day in range(2,n+1):
            if know and know[0][0] == day-delay:
                shareCnt += know[0][1]
                knowCnt -= know[0][1]
                share.append(know[0])
                know.popleft()
            if share and share[0][0] == day-forget:
                shareCnt -= share[0][1]
                share.popleft()
            if share:
                knowCnt += shareCnt
                know.append((day,shareCnt))
        return (knowCnt + shareCnt)%(10**9+7) 