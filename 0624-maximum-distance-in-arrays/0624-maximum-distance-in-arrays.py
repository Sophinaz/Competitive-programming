class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        largest, large, small, smallest = [float('-inf'),0], [float('-inf'), 0], [float('inf'),0], [float('inf'), 0]

        for i in range(len(arrays)):
            if arrays[i][0] < smallest[0]:
                small = smallest
                smallest = [arrays[i][0], i]
            elif smallest[0] <= arrays[i][0] < small[0]:
                small = [arrays[i][0], i]
            if arrays[i][-1] > largest[0]:
                large = largest
                largest = [arrays[i][-1], i]
            elif large[0] < arrays[i][-1] <= largest[0] :
                large = [arrays[i][-1], i]

        # print(largest, large, small, smallest)
        res = []
        if largest[1] != smallest[1]: res.append(largest[0] - smallest[0])
        if largest[1] != small[1]: res.append(largest[0] - small[0])
        if large[1] != smallest[1]: res.append(large[0] - smallest[0])
        if large[1] != small[1]: res.append(large[0] - small[0])
        if res: return max(res)
        return 0

        