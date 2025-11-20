class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        points = []
        
        for start, end in intervals:
            count = 0
            for point in points[-2:]: 
                if start <= point <= end:
                    count += 1
            
            if count == 0:
                points.append(end - 1)
                points.append(end)
            elif count == 1:
                points.append(end)
                
        return len(points)