class Solution:
    def maxArea(self, height: List[int]) -> int:
        def maxar(height):
            l,r = 0,len(height)-1
            max_area = 0
            while l<r:
                temp = min(height[l],height[r]) * (r-l)
                max_area = max(max_area,temp)
                if height[l] < height[r]:
                    l+=1
                else:
                    r-=1
            return max_area
        return maxar(height)

        