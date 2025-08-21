class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        res = []
        n = len(digits)
        if n == 0: return res
        def backtrack(idx,cur):
            if idx == n:
                res.append("".join(cur))
                return
            for char in hash_map[digits[idx]]:
                cur.append(char)
                backtrack(idx+1,cur)
                cur.pop()
        backtrack(0,[])
        return res