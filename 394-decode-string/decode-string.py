class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ''
        cur_num = 0
        for char in s:
            if char == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ''
                cur_num = 0
            elif char == ']':
                prev_num = stack.pop()
                prev_str = stack.pop()
                cur_str = prev_str + cur_str*prev_num
            elif char.isdigit():
                cur_num = cur_num*10 + int(char)
            else :
                cur_str += char
        return cur_str