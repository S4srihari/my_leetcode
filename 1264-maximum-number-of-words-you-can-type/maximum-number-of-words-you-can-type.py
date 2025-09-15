class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        res = 0
        for word in words:
            found = False
            for c in brokenLetters:
                if c in set(word):
                    found = True
                    break
            res += 1 if not found else 0
        return res