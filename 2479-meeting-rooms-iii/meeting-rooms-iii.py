class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # finding the roon that is used the most
        # meeting always helds in first room available
        meetings.sort()
        room_meetings = [0]*n
        next_available_time = [0]*n
        for start,end in meetings:
            min_idx = 0
            executed = False
            for i in range(n):
                if next_available_time[i] <= start :
                    room_meetings[i] += 1
                    next_available_time[i] = end
                    executed = True
                    break
                elif next_available_time[i] < next_available_time[min_idx]:
                    min_idx = i
            if not executed:
                room_meetings[min_idx] += 1
                next_available_time[min_idx] += end - start

        res_room = 0
        max_meets = 0
        for i in range(n):
            if room_meetings[i] > max_meets:
                res_room = i
                max_meets = room_meetings[i]
        return res_room