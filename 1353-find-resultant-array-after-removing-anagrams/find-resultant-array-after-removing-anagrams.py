class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if not words: return []
        res = []
        res.append(words[0])

        def compare(a,b):
            freq = [0]*26
            for c in a:
                freq[ord(c)-ord('a')] += 1
            for c in b:
                freq[ord(c) - ord('a')] -= 1
            return all(j == 0 for j in freq)

        for i in range(1,len(words)):
            if not compare(res[-1],words[i]):
                res.append(words[i])
                
        return res