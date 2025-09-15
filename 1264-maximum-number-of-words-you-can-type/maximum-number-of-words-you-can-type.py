class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        res = 0
        for word in words:
            if any([c in word for c in brokenLetters]):
                continue
            else:
                res += 1
        return res