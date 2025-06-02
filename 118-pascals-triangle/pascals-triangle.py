class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            if i == 0:
                ans.append([1])
            else:
                temp = [1]
                for j in range(len(ans[-1])-1):
                    temp.append(ans[-1][j]+ans[-1][j+1])
                temp.append(1)
                ans.append(temp)
        return ans