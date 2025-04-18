class Solution:
    def countAndSay(self, n: int) -> str:
        if n < 2 :
            return '1'
        elif n == 2:
            return '11'
        cas = '11'
        for _ in range(3,n+1):
            temp_cnt = 1
            temp = ''
            for i in range(1,len(cas)):
                if cas[i] != cas[i-1] and i == len(cas) - 1:
                    temp = temp + str(temp_cnt) 
                    temp += cas[i-1]
                    temp_cnt = 1
                    temp += str(temp_cnt) 
                    temp += cas[i]
                elif cas[i] != cas[i-1]:
                    temp = temp + str(temp_cnt) 
                    temp += cas[i-1]
                    temp_cnt = 1
                elif i == len(cas) - 1:
                    temp_cnt += 1
                    temp += str(temp_cnt)
                    temp += cas[i]
                else :
                    temp_cnt += 1
            cas = temp
            
        return cas