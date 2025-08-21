class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l,m = len(board),len(board[0])
        n = len(word)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def backtrack(i,j,idx,visited):
            if idx == n:
                return True
            visited.add((i,j))
            for di,dj in dirs:
                if 0 <= i+di < l and 0 <= j+dj < m and board[i+di][j+dj] == word[idx] and (i+di,j+dj) not in visited:
                    if backtrack(i+di,j+dj,idx+1,visited):
                        return True
            visited.remove((i,j))
            return False

        for i in range(l):
            for j in range(m):
                if board[i][j] == word[0]:
                    if backtrack(i,j,1,set()):
                        return True

        return False