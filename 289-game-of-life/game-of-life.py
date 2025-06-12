class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        prev = []
        prev2 = []
        for i in range(m):
            cur = []
            for j in range(n):
                cnt = 0
                for di in range(-1,2):
                    for dj in range(-1,2):
                        if di == 0 and dj == 0:
                            continue
                        elif i+di > -1 and i +di < m and j+dj > -1 and j+dj < n:
                            cnt += board[i+di][j+dj]
                if board[i][j] == 1:
                    if cnt < 2:
                        cur.append(0)
                    elif cnt < 4:
                        cur.append(1)
                    else:
                        cur.append(0)
                else :
                    if cnt == 3:
                        cur.append(1)
                    else :
                        cur.append(0)
            if i > 1:
                board[i-2] = prev2
            prev2 = prev
            prev  = cur
        if m > 1: 
            board[-2] = prev2
        if m > 0 :
            board[-1] = prev