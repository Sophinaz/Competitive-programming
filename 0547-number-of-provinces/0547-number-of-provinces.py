class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        graph = defaultdict(list)
        result = 0
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1 and row != col:
                    graph[row+1].append(col+1)

        def dfs(curr, visited):
            print(visited)
            visited[curr-1] = True
            for neighbour in graph[curr]:
                if not visited[neighbour-1]:
                    dfs(neighbour, visited)


        for curr in range(len(isConnected)):
            if not visited[curr]:
                result += 1
                dfs(curr+1, visited)
        return result

