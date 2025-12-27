class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # finding the roon that is used the most
        # first meeting always starts in first room
        meetings.sort()
        room_meetings = [0]*n
        next_available_time = [0]*n
        heapq.heapify(next_available_time)
        for start,end in meetings:
            ends_fast = 0
            executed = False
            for i in range(n):
                if next_available_time[i] <= start :
                    room_meetings[i] += 1
                    next_available_time[i] = end
                    executed = True
                    break
                elif next_available_time[i] < next_available_time[ends_fast]:
                    ends_fast = i
            if not executed:
                room_meetings[ends_fast] += 1
                next_available_time[ends_fast] += end - start

        res = 0
        max_meets = 0
        for i in range(n):
            if room_meetings[i] > max_meets:
                res = i
                max_meets = room_meetings[i]
        return res