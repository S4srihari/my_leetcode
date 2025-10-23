class Solution:
    def hasSameDigits(self, s: str) -> bool:
        que = deque([int(i) for i in s])
        temp = deque([])
        while len(que) > 2:
            for i in range(len(que)-1):
                val1 = que.popleft()
                val2 = que[0]
                temp.append((val1+val2)%10)
            que,temp = temp,que
            temp.clear()
        return que[0] == que[1]