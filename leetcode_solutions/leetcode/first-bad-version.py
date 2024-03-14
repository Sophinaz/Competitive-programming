# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        while left <= n:
            mid = (n + left) // 2
            ans = isBadVersion(mid)

            if ans:
                n = mid-1
            else:
                left = mid+1

        return left