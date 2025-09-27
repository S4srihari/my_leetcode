class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        if n < 3: return 0
        maxArea = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    a = abs(((points[i][0]-points[j][0])**2 +(points[i][1]-points[j][1])**2)**0.5)
                    b = abs(((points[k][0]-points[j][0])**2 +(points[k][1]-points[j][1])**2)**0.5)
                    c = abs(((points[i][0]-points[k][0])**2 +(points[i][1]-points[k][1])**2)**0.5)
                    s = (a+b+c)/2
                    if s<a or s<b or s<c: continue
                    area = (s*(s-a)*(s-b)*(s-c))**0.5
                    maxArea = max(area,maxArea)
        return maxArea