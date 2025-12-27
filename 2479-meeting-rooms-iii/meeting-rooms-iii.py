class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # finding the roon that is used the most
        # meeting always helds in first room available
        meetings.sort()
        count = [0]*n
        ready_rooms = [i for i in range(n)]
        heapq.heapify(ready_rooms)
        busy_rooms = []

        for start,end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(ready_rooms, room)
            
            if ready_rooms:
                room = heapq.heappop(ready_rooms)
                heapq.heappush(busy_rooms, (end, room))
                count[room] += 1
            
            else:
                end_time, room = heapq.heappop(busy_rooms)
                new_end_time = end_time + end - start
                count[room] += 1
                heapq.heappush(busy_rooms, (new_end_time, room))

        max_room = 0
        max_meets = 0
        for i in range(n):
            if count[i] > max_meets:
                res_room = i
                max_meets = count[i]
        return res_room