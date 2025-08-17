class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        digs = {'1':1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
        strs = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",0:"0"}
        res = 0
        n = len(num1)
        idx = 0
        while idx < n:
            cur = num1[idx]
            temp = 0
            for i in num2:
                temp *= 10
                temp += digs[cur]*digs[i]
            res *= 10
            res += temp
            idx += 1
        ans = ""
        while res > 0:
            ans = ans + strs[res%10]
            res = res//10
        return ans[::-1]