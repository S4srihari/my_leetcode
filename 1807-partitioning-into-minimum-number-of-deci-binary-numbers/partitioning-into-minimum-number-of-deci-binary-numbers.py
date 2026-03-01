class Solution:
    def minPartitions(self, n: str) -> int:
        return max(set(int(i) for i in n))