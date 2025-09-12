class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        for ch in s:
            if ch in "aeiouAEIOU" :
                vowels.append(ch)
        vowels.sort()
        res = []
        idx = 0
        for ch in s:
            if ch not in "aeiouAEIOU":
                res.append(ch)
            else:
                res.append(vowels[idx])
                idx += 1
        return "".join(res)