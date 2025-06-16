class Solution:
    def reachNumber(self, target: int) -> int:
        if target == 0: return 0
        target = abs(target)
        total,steps = 0,1
        while total < target:
            total += steps
            steps += 1
        while (total-target)%2 == 1:
            total += steps
            steps += 1
        return steps - 1