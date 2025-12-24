class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        tot = sum(apple)
        capacity.sort(reverse = True)
        res = 1
        for slots in capacity:
            if slots >= tot:
                return res
            tot -= slots
            res += 1
        return res 