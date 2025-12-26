class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prev_penalty = [0]*(n+1)
        fut_penalty = [0]*(n+1)
        tot_hrs_with_cust = 0
        tot_hrs_without_cust = 0
        for i in range(n):
            if i < n and customers[i] == "Y":
                tot_hrs_with_cust += 1
            elif i < n:
                tot_hrs_without_cust += 1
            prev_penalty[i+1] = tot_hrs_without_cust

        for i in range(n+1):
            fut_penalty[i] = tot_hrs_with_cust
            if i < n and customers[i] == "Y":
                tot_hrs_with_cust -= 1
        
        res = n+1
        min_seen_penalty = float("inf")
        for i in range(n+1):
            tot_penalty = prev_penalty[i] + fut_penalty[i]
            if tot_penalty < min_seen_penalty:
                res = i
                min_seen_penalty = tot_penalty
        return res