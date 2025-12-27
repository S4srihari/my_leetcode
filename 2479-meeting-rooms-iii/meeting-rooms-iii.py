class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # finding the roon that is used the most
        # meeting always helds in first room available
        meetings.sort()
        count = [0]*n
        ready_at = [0]*n
        for start,end in meetings:
            min_idx = 0
            for i in range(n):
                if ready_at[i] < ready_at[min_idx]:
                    min_idx = i
                if ready_at[i] <= start :
                    count[i] += 1
                    ready_at[i] = end
                    break
            else:
                count[min_idx] += 1
                ready_at[min_idx] += end - start

        res_room = 0
        max_meets = 0
        for i in range(n):
            if count[i] > max_meets:
                res_room = i
                max_meets = count[i]
        return res_room