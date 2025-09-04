class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        p1 = abs(x-z)
        p2 = abs(y-z)
        if p1 < p2:
            return 1  
        elif p1 > p2:
            return 2
        else :
            return 0