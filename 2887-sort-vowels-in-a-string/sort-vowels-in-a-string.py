class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        for ch in s:
            if ch in "aeiouAEIOU" :
                vowels.append(ch)
        vowels.sort()
        res = ""
        idx = 0
        for ch in s:
            if ch not in "aeiouAEIOU":
                res += ch
            else:
                res += vowels[idx]
                idx += 1
        return res