# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0

        while True:
            num = (n + left) // 2
            ans = isBadVersion(num)

            if ans:
                # if not isBadVersion(num-1):
                #     return num
                n = num-1
            else:
                if isBadVersion(num+1):
                    return num+1
                left = num+1