class Solution:
    def countCollisions(self, directions: str) -> int:
        r_cnt = 0
        stay = False
        res = 0
        for car in directions:
            if car == "S":
                if r_cnt > 0:
                    res += r_cnt
                    r_cnt = 0
                stay = True
            elif car == "L":
                if r_cnt > 0:
                    res += 1+r_cnt
                    stay = True
                    r_cnt = 0
                elif stay:
                    res += 1
            else:
                r_cnt += 1
        return res
