class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:
    def __init__(self):
        self.start = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.start
        for char in word:
            if char not in node.children:
                new_node = TrieNode()
                node.children[char] = new_node
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.start
        def dfs(node, idx):
            if not node:
                return False

            if idx == len(word): 
                if node.end:
                    return True
                return False

            if word[idx] != "." and word[idx] not in node.children:
                return False

            res = False
            if word[idx] != ".":
                res = res or dfs(node.children[word[idx]], idx+1)
            else:
                for child in node.children:
                    res = res or dfs(node.children[child], idx+1)
            
            return res
        return dfs(node, 0)

            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)