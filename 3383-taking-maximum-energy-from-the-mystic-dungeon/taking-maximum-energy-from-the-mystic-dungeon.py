class Solution:
    def helper(self, i, energy, k):
        if i < 0: return 0
        prev = self.helper(i-k, energy, k)
        return energy[i] + prev if prev > 0 else energy[i]
        

    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        res = float("-inf")
        for i in range(n-1,n-1-k,-1):
            if i >= 0:
                res = max(res, self.helper(i,energy, k))
            else:
                break
        return res