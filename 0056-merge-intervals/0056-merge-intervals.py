class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            if not result:
                result.append(intervals[i])
                continue

            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append(intervals[i])

        return result