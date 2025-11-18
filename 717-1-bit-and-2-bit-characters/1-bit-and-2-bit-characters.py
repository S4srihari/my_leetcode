class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        l = len(bits)
        if l == 1: return True
        elif bits[-2] == 0: return True
        else:
            idx =  l-2
            cnt = 0
            while idx >= 0 and bits[idx] == 1:
                idx -= 1
                cnt += 1
            return True if cnt%2 == 0 else False