class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        max_y, tot = 0, 0
        for x, y, l in squares:
            max_y = max(max_y, y + l)
            tot += l**2

        
        def calculate(idx):
            area_below = 0
            for _, y, l in squares:
                if y < idx :
                    area_below += l * min(idx-y, l)
            return area_below >= tot/2

        eps = 1e-5
        left, right = 0, max_y
        while abs(left - right) > eps:
            mid = (left + right)/2
            if calculate(mid):
                right = mid 
            else:
                left = mid
        return right

