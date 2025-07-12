class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse = True)
        stack = []
        for p,s in pair:
            time = (target - p)/s
            if not stack or stack[-1] < time:
                fleets += 1
                stack.append(time)
        return fleets 