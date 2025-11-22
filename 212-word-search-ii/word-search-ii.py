class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        m,n = len(board), len(board[0])
        res, vis = [], set()

        def dfs(i,j, node, word):
            if (i<0 or j<0 or i>=m or j>=n or (i,j) in vis or board[i][j] not in node.children):
                return
            vis.add((i,j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.isWord :
                res.append(word)
                node.isWord = False
            
            for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
                dfs(i+di, j+dj, node, word)
            
            vis.remove((i,j))

        for row in range(m):
            for col in range(n):
                dfs(row,col,root,"")
        return res