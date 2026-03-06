class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if s.count('0') == 0: return True
        z_idx = s.find('0')
        return s[z_idx:].count('1') == 0