class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def checker(number):
            count = 0
            for i in citations:
                if i >= number:
                    count += 1
                if count == number:
                    return True

            return False

        left, right = 0, max(citations)

        while left <= right:
            mid = (left + right) // 2

            if checker(mid):
                left = mid + 1
            else:
                right = mid - 1

        return left - 1