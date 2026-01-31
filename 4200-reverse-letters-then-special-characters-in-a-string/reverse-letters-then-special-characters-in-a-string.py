class Solution:
    def reverseByType(self, s: str) -> str:
        char_types = []
        letters = []
        special = []

        for i in range(len(s)):
            if s[i].isalpha():
                char_types.append(1)
                letters.append(s[i])
            else:
                char_types.append(2)
                special.append(s[i])
        
        res = []
        for i in range(len(s)):
            if s[i].isalpha():
                res.append(letters.pop())
            else:
                res.append(special.pop())
        return "".join(res)