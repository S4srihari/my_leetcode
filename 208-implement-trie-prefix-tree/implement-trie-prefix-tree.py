class Node:
    def __init__(self):
        self.children = {}
        self.EoW = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if not word[i] in  node.children:
                node.children[word[i]] = Node()
            node = node.children[word[i]]
        node.EoW = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            if not word[i] in node.children:
                return False
            node = node.children[word[i]]
        return node.EoW

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if not prefix[i] in node.children:
                return False
            node = node.children[prefix[i]]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)