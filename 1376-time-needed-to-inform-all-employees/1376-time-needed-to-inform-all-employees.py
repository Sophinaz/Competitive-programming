class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        result = [0 for i in range(len(manager))]
        visited = set()
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].append(i)

        def dfs(node):
            visited.add(node)
            for child in graph[node]:
                result[child] += (result[node] + informTime[node])
                if child not in visited:
                    dfs(child)
        dfs(headID)
        return max(result)