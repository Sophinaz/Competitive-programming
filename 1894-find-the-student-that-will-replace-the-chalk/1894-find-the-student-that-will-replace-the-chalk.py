class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        divisor = k // total
        remain = k - (divisor * total)

        for i in range(len(chalk)):
            if remain < chalk[i]:
                return i
            remain -= chalk[i]
            