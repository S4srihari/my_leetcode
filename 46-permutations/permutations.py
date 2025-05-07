class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        lis = []
        def recurse(a,b):
            if not b:
                lis.append(a)
                return
            for i in range(len(b)):
                left = a.copy()
                right = b.copy()
                left.append(b[i])
                right.pop(i)
                recurse(left,right)
            return 
        recurse([],nums)
        return lis
                