class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_cords = [[n+2, -1] for _ in range(n+1)]
        y_cords = [[n+2, -1] for _ in range(n+1)]
        cnt = 0
        for x,y in buildings:
            if x_cords[y][0] > x:
                x_cords[y][0] = x
            if x_cords[y][1] < x:
                x_cords[y][1] = x

            if y_cords[x][0] > y: 
                y_cords[x][0] = y
            if y_cords[x][1] < y:
                y_cords[x][1] = y
        
        
        for x,y in buildings:
            if x_cords[y][0] < x and x_cords[y][1] > x and y_cords[x][0] < y and y_cords[x][1] > y:
                cnt += 1
        return cnt