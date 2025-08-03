class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        keys = sorted(list(c.keys()))
        for key in keys:
            if c[key] > 0:
                groups = c[key]
                for j in range(groupSize):
                    if key+j not in c or c[key+j] < groups:
                        return False
                    else : c[key+j] -= groups
        return True