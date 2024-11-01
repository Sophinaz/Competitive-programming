class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letterCount = Counter(tasks)
        count = Counter(letterCount.values())

        result = 0
        for i in count:
            diff = n - (count[i]-1)
            if diff < 0:
                diff = 0
            result += (i * count[i]) + ((i-1) * (diff))

        return result