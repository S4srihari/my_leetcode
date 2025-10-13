class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if not words: return []
        res = []
        res.append(words[0])
        prev = Counter(words[0])
        for i in range(1,len(words)):
            cur = Counter(words[i])
            if prev != cur:
                res.append(words[i])
                prev = cur
        return res