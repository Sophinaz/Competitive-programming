class Node:
    def __init__(self, char = ""):
        self.children = {}
        self.char = char
        self.isend = False
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Node()
        def insert(word):
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node(c)
                curr = curr.children[c]
            curr.isend = True

        for word in words:
            insert(word)

        def dfs(node):
            res = []
            for child in node.children:
                if node.children[child].isend:
                    x = dfs(node.children[child])
                    if len(x) > len(res) or (len(x) == len(res) and x < res):
                        res = x

            return [node.char] + res

        return ''.join(dfs(root))