class RecentCounter:

    def __init__(self):
        self.stack = []
        self.idx = 0
    def ping(self, t: int) -> int:
        self.stack.append(t)
        while self.stack[self.idx] < t-3000:
            self.stack.pop(0)
        return len(self.stack)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)