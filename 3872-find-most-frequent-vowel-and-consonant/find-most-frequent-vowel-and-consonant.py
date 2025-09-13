class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = [0]*26
        for c in s:
            freq[ord(c)-ord('a')] += 1
        maxVowelFreq = 0
        for i in (0,4,8,14,20):
            if freq[i] > maxVowelFreq:
                maxVowelFreq = freq[i]
            freq[i] = 0
        maxConsFreq = max(freq)
        return maxVowelFreq + maxConsFreq