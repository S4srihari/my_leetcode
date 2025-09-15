class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        found = 0
        for word in text.split():
            for letter in word:
                if letter in brokenLetters:
                    found += 1
                    break
        return len(text.split())-found