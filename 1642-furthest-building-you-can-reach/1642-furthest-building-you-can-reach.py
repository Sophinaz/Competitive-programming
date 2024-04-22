class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            gap = heights[i+1] - heights[i]
            if gap > 0:
                heappush(heap, gap)
                if ladders > 0:
                    ladders -= 1
                else:
                    x = heappop(heap)
                    if x <= bricks:
                        bricks -= x
                    else:
                        return i
        return len(heights)-1

