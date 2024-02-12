class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        node = Node(homepage)
        self.currentpage = node

    def visit(self, url: str) -> None:
        node = Node(url)
        self.currentpage.next = node
        node.prev = self.currentpage
        self.currentpage = node

    def back(self, steps: int) -> str:
        curr = self.currentpage
        while steps > 0 and curr.prev:
            curr = curr.prev
            steps -= 1
        self.currentpage = curr
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.currentpage
        while steps > 0 and curr.next:
            curr = curr.next
            steps -= 1
        self.currentpage = curr
        return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)