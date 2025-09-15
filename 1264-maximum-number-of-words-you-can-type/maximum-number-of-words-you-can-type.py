class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        found = 0
        for word in words:
            for letter in word:
                if letter in brokenLetters:
                    found += 1
                    break
        return len(words)-found