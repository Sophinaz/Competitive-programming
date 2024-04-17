class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        for i in range(len(nums)):
            nums[i] = nums[i] * -1
        self.maxheap = nums
        heapify(self.maxheap)
        self.minheap = []
        
        for _ in range(k-1):
            heappush(self.minheap,-1 *  heappop(self.maxheap))
        heapify(self.minheap)

    def add(self, val: int) -> int:
        if not self.maxheap or val <= -1 * self.maxheap[0]:
            heappush(self.maxheap, -1 * val)
        else:
            if self.minheap: 
                heappush(self.maxheap, -1 * heappop(self.minheap))
                heappush(self.minheap, val)
            else:heappush(self.maxheap, -1 * val)

        return -1 * self.maxheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)