class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        row = 0
        step = 1
        arr = [''] * numRows

        for c in s:
            arr[row] += c

            if row == 0:
                step = 1
            elif row == numRows-1:
                step = -1

            row += step

        return ''.join(arr)