class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        n = len(s)
        prefix_val = [0] * (n + 1)
        prefix_sum = [0] * (n + 1)
        prefix_count = [0] * (n + 1)
        
        curr_val = 0
        curr_sum = 0
        curr_cnt = 0
        
        for i, char in enumerate(s):
            digit = int(char)
            if digit != 0:
                curr_val = (curr_val * 10 + digit) % mod
                curr_cnt += 1
            curr_sum += digit
            prefix_val[i+1] = curr_val
            prefix_sum[i+1] = curr_sum
            prefix_count[i+1] = curr_cnt
            
        res = []
        for l, r in queries:
            count = prefix_count[r+1] - prefix_count[l]
            if count == 0:
                res.append(0)
                continue
            
            digit_sum = prefix_sum[r+1] - prefix_sum[l]
            diff = prefix_count[r+1] - prefix_count[l]
            num_val = (prefix_val[r+1] - (prefix_val[l] * pow(10, diff, mod))) % mod
            ans = (num_val * digit_sum) % mod
            res.append(ans)
            
        return res