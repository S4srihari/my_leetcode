class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        freq = defaultdict(list)
        m,n = len(mat), len(mat[0])
        """rev = False
        for idx_sum in range(m+n-1):    
            temp = []
            for i in range(min(m,idx_sum+1)):
                for j in range(min(n,idx_sum+1)):
                    if i+j == idx_sum:
                        temp.append(mat[i][j])
            if not rev :
                res.extend(temp[::-1])
            else : res.extend(temp)
            rev = not rev"""
        for i in range(m):
            for j in range(n):
                freq[i+j].append(mat[i][j])
        ans = []
        for i in range(m+n-1):
            ans.extend(freq[i] if i%2!=0 else freq[i][::-1])
        return ans