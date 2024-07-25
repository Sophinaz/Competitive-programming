class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        numofnodes = []
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def dfs(n):
            stack = [n]
            visited.add(n)
            count = 1
            while stack:
                node = stack.pop()
                for child in graph[node]:
                    if child not in visited:
                        stack.append(child)
                        visited.add(child)
                        count += 1
            numofnodes.append(count)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
        result = []
        for i in range(len(numofnodes)):
            for j in range(i+1, len(numofnodes)):
                result.append(numofnodes[i] * numofnodes[j])
        
        return sum(result)