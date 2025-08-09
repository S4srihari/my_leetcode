class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []
        if n == 0: return res
        def canExpress(idx,path,cur,prev):
            if idx == len(num):
                if cur == target:
                    res.append(path)
                return
            
            for i in range(idx,n):
                if i > idx and num[idx] == '0': break
                val = int(num[idx:i+1])
                if idx  == 0:
                    canExpress(i+1,path+str(val),cur+val,val)
                else:
                    canExpress(i+1,path+"+"+str(val),cur+val,val)
                    canExpress(i+1,path+"-"+str(val),cur-val,-val)
                    canExpress(i+1,path+"*"+str(val),cur-prev + (prev*val), prev*val)
            
        canExpress(0,"",0,0)
        return res
