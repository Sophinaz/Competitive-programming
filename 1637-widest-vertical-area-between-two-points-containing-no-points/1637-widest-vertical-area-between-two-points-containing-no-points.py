class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        result = 0
        left,right = 0,1

        while right < n:
            result = max(result,points[right][0] - points[left][0])
            left += 1
            right += 1

        return result
