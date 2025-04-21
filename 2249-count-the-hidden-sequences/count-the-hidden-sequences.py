class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        low, high = 0, 0
        tot = 0
        for diff in differences:
            tot += diff
            if tot < low:
                low = tot
            if tot > high:
                high = tot
        posseq = (upper-lower) - (high-low) + 1
        if posseq > 0:
            return posseq
        else :
            return 0