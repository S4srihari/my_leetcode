class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """hash = set()
        s_len = len(s)
        for word in wordDict :
            n = len(word)
            if n > s_len:
                continue
            for i in range(s_len - n + 1):
                if s[i:i+n] == word:
                    hash.add((i,i+n-1))
        hash = list(sorted(hash))
        for i in range(1,len(hash)):
            for j in range(len(hash)):
                if hash[j][1] + 1 == hash[i][0]:
                    hash.append((hash[j][0],hash[i][1]))
        return (0,s_len-1) in hash"""


        dp= [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(i))

        return dp[len(s)]