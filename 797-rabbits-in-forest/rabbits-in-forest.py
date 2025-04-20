class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        ret = 0
        for i in c:
            ret += (c[i]//(i+1))*(i+1) 
            if c[i]%(i+1) > 0:
                ret += (i + 1)
        return ret