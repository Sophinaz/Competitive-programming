class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 1
        right = n
        totala, totalb = 0,0

        while left <= right:
            if left == right and totala == totalb:
                return left

            if totala <= totalb:
                totala += left
                left += 1
            else: 
                totalb += right
                right -= 1
        return -1