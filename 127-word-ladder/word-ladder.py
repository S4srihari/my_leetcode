class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        que = deque()
        que.append((beginWord, 1))
        wordList = set(wordList)
        if beginWord in wordList: wordList.remove(beginWord)
        n = len(beginWord)
        while que:
            word, level = que.popleft()
            if word == endWord:
                return level
            for i in range(n):
                for alp in range(26):
                    char = chr(ord('a')+alp)
                    if word[:i] + char + word[i+1:] in wordList:
                        que.append((word[:i] + char + word[i+1:],level+1))
                        wordList.remove(word[:i] + char + word[i+1:])
        return 0

