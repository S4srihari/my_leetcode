class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_logs = []
        dig_logs = []
        for log in logs:
            if log[-1].isdigit():
                dig_logs.append(log)
            elif log[-1].isalpha():
                lis = log.split()
                s = (" ".join(lis[1:]), lis[0])
                let_logs.append(s)
        let_logs.sort()
        res = []
        for log in let_logs:
            lis = log[0].split()
            s = log[1] + " " + " ".join(lis)
            res.append(s)
        res.extend(dig_logs)
        return res
