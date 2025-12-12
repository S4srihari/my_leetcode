class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key = lambda x: (int(x[1]), -ord(x[0][0])))
        offline = {}
        res = [0]*numberOfUsers
        for event in events:
            if event[0] == "OFFLINE":
                offline[int(event[2])] = int(event[1])
            else:
                activated = set()
                for i in offline:
                    if offline[i] + 60 <= int(event[1]):
                        activated.add(i)
                for i in activated:
                    del offline[i]
                if event[2] == "ALL":
                    res = [i+1 for i in res]
                elif event[2] == "HERE":
                    for i in range(numberOfUsers):
                        if i not in offline:
                            res[i] += 1 
                else:
                    for i in event[2].split(" "):
                        idx = int(i[2:])
                        res[idx] += 1
        return res