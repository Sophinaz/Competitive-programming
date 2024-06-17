class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1: return 1
        graph = defaultdict(list)
        check = set()
        for a, b in trust:
            graph[b].append(a)
            check.add(a)

        for i in graph:
            if len(graph[i]) == n-1 and i not in check:
                return i
        return -1