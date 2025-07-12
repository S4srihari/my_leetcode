class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse = True)
        stack = []
        prev = 0
        for p,s in pair:
            time = (target - p)/s
            if prev < time:
                fleets += 1
                prev = time
        return fleets 