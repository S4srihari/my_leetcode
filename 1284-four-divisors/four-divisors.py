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
        tot = 0
        for num in nums:
            divs = self.get_divisors(num)
            if len(divs) == 4:
                tot += sum(divs)
        return tot