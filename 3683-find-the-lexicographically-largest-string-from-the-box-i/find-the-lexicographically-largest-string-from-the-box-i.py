class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        l_len = n - numFriends + 1
        res = ""
        for i in range(n):
            if  word[i:i+l_len] > res:
                res = word[i:i+l_len]  
        return res