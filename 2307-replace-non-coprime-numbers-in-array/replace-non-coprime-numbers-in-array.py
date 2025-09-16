class Solution:
    def gcd(self,a,b):
        return math.gcd(a,b)
    def lcm(self,a,b):
        return a*b//self.gcd(a,b)
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack and self.gcd(stack[-1],num)>1:
                temp = stack.pop()
                num = self.lcm(num,temp)
            stack.append(num)
        return stack 