class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        res,prefix_sum = 0,0
        for i in range(len(gas)):
            prefix_sum += gas[i]-cost[i]
            if prefix_sum <0:
                prefix_sum = 0
                res = i+1
        return res  