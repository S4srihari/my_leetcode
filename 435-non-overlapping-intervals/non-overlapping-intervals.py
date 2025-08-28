class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  
        count, end = 0, float('-inf')

        for start, finish in intervals:
            if start >= end:  
                end = finish
            else:             
                count += 1

        return count