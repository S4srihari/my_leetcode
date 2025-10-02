class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        prev = [1,1]
        cur = []
        for i in range(2,rowIndex+1):
            cur = [1]
            for j in range(i-1):
                cur.append(prev[j]+prev[j+1])
            cur.append(1)
            prev,cur = cur,prev
        return prev