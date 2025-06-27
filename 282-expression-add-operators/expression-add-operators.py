class Solution:
    def value_equals_target(self,lis,target):
        res = []
        for equation in lis:
            stack = []
            num = 0
            sign = '+'
            temp = deque(equation)
            while temp:
                char = temp.popleft()
                if char.isdigit():
                    num = num * 10 + int(char)
                if char in '+-*' or not temp:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    sign = char
                    num = 0

            if sum(stack) == target:
                res.append(equation)
        return res
            
    def addOperators(self, num: str, target: int) -> List[str]:
        if len(num) == 1 and int(num) == target:
            return [num]
        elif len(num) == 1:
            return []
        store_pos = []
        def operation(num,cur):
            operators = ['*','+','-','']
            if not num:
                store_pos.append(cur)
                return
            temp = cur
            for op in operators:
                if op == '':
                    last_num = cur.split('+')[-1].split('-')[-1].split('*')[-1]
                    if last_num == '0':
                        continue
                cur = cur + op + num[0]
                operation(num[1:], cur)
                cur = temp
                    
        operation(num[1:],num[0])
        
        return  self.value_equals_target(store_pos,target)