class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = defaultdict(list)
        for hr in range(12):
            cnt = str(bin(hr)).count('1')
            hours[cnt].append(str(hr))
        minutes = defaultdict(list)
        for mn in range(60):
            cnt = str(bin(mn)).count('1')
            if mn < 10:
                minutes[cnt].append("0"+str(mn))
            else:
                minutes[cnt].append(str(mn))
        
        res = []
        for hr_cnt in range(turnedOn+1):
            if hr_cnt > 3:
                break
            for hr in hours[hr_cnt]:
                for minute in minutes[turnedOn - hr_cnt]:
                    res.append(hr+":"+minute)
        return res