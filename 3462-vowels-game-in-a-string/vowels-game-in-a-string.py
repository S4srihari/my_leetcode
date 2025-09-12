class Solution:
    def doesAliceWin(self, s: str) -> bool:
        """for c in s:
            if c in "aeiou":
                return True
        return False"""

        return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") > 0