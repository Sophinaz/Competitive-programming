class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        answer = []
        i = 0
        for a,b in intervals:
            if a < newInterval[0]:
                result.append([a,b])
            else:
                break
            i += 1
        result.append(newInterval)
        result.extend(intervals[i:])
        print(result)

        for idx in range(len(result)):
            a, b = result[idx]
            if not answer:
                answer.append([a,b])
                continue

            if a <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], b)
            else:
                answer.append([a,b])

        return answer