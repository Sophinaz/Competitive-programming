class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if not self.maxheap:  
            heappush(self.maxheap, -1 * num)
            return
         
        if num > (-1 * self.maxheap[0]) and (not self.minheap or num > self.minheap[0]):
            if len(self.minheap) <= len(self.maxheap):
                heappush(self.minheap, num)
            else:
                x = heappop(self.minheap)
                heappush(self.maxheap, -1 * x)
                heappush(self.minheap, num)
        else:
            if len(self.maxheap) <= len(self.minheap):
                heappush(self.maxheap, -1 * num)
            else:
                heappush(self.minheap, -1 * heappop(self.maxheap))
                heappush(self.maxheap, -1 * num)
        print(self.maxheap, self.minheap)


    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -1 * self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            if self.maxheap and self.minheap:
                return ((-1 * self.maxheap[0]) + self.minheap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()