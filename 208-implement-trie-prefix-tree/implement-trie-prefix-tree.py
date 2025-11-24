class Node:
    def __init__(self):
        self.children = {}
        self.EoW = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not ch in  node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.EoW = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if not ch in node.children:
                return False
            node = node.children[ch]
        return node.EoW

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if not ch in node.children:
                return False
            node = node.children[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)