class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        nums = sorted(points)
        print(nums)
        left,right,result = 0,0,0
        n = len(nums)
        
        while right < n:
            if nums[left][0] <= nums[right][0] <= nums[left][1]:
                nums[left][0] = nums[right][0]
                nums[left][1] = min(nums[left][1],nums[right][1])
                right += 1
            else:
                result += 1
                left = right
                right += 1
        return result+1