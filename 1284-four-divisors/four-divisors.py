class Solution:
    def get_divisors(self, num):
        divisors = set()
        limit = num ** 0.5
        i = 1
        while(i <= limit):
            if(num % i == 0):
                divisors.add(i)
                poss_div = num//i
                divisors.add(poss_div)
            i += 1
        return divisors

    def sumFourDivisors(self, nums: List[int]) -> int:
        m = max(nums)
        divs = [0 for i in range(m+1)]
        sums = [0 for i in range(m+1)]
        for i in range(1,m+1,1):
            for j in range(i,m+1,i):
                divs[j]+=1
                sums[j]+=i
        res = 0
        for i in nums:
            if divs[i] == 4:
                res+=sums[i]
        
        return res