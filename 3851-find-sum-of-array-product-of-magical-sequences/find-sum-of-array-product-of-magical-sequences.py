class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        self.MOD = 10**9 + 7
        self.m = m
        self.k = k
        self.nums = nums
        self.n = len(nums)
        self.memo = {}

        if m == 0:
            return 1 if k == 0 else 0

        self.max_bits = k + 1
        self.C = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            self.C[i][0] = 1
            for j in range(1, i + 1):
                self.C[i][j] = (self.C[i-1][j-1] + self.C[i-1][j]) % self.MOD

        self.pows = [[0] * (m + 1) for _ in range(self.n)]
        for i in range(self.n):
            self.pows[i][0] = 1
            for j in range(1, m + 1):
                self.pows[i][j] = (self.pows[i][j-1] * self.nums[i]) % self.MOD
        
        result_array = self.solve(0, m, 0)
        
        return result_array[k]

    def solve(self, i: int, j: int, carry: int) -> List[int]:
        if j == 0:
            # The remaining carry contributes to the bit count.
            k_bits = bin(carry).count('1')
            res = [0] * self.max_bits
            if k_bits < self.max_bits:
                res[k_bits] = 1  # Product of an empty set of future choices is 1.
            return res

        # Base case: out of numbers, but still need to place elements. Impossible path.
        if i == self.n:
            return [0] * self.max_bits
        
        state = (i, j, carry)
        if state in self.memo:
            return self.memo[state]
        
        total_res = [0] * self.max_bits
        
        # Iterate on p, the number of times we use index i.
        for p in range(j + 1):
            # Recurse for the next index `i+1` with `j-p` elements left to choose.
            # The new carry is calculated from the current choices `p` and previous `carry`.
            new_carry = (p + carry) // 2
            res_from_recursion = self.solve(i + 1, j - p, new_carry)
            
            # The bit value at the current position `i`.
            current_bit = (p + carry) % 2
            
            # Product contribution: (ways to choose p slots) * (product from these p choices)
            term_prod = (self.C[j][p] * self.pows[i][p]) % self.MOD
            
            # Combine the current result with the results from the recursive call.
            for k_bits in range(self.max_bits):
                if res_from_recursion[k_bits] > 0:
                    new_k_bits = k_bits + current_bit
                    if new_k_bits < self.max_bits:
                        contribution = (term_prod * res_from_recursion[k_bits]) % self.MOD
                        total_res[new_k_bits] = (total_res[new_k_bits] + contribution) % self.MOD

        self.memo[state] = total_res
        return total_res