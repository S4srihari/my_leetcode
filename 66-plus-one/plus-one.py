class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits : 
            return []
        idx = len(digits) - 1
        while idx >= 0 and digits[idx] == 9:
            digits[idx] = 0
            idx -= 1
        if idx >= 0:
            digits[idx] += 1
        else:
            digits.insert(0,1)
        return digits