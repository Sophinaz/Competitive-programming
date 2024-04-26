class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = {i:i for i in range(n)}
        rank = [0 for i in range(n)]
        track = defaultdict(int)
        result = 0
        def find(num):
            while num != parent[num]:
                parent[num] = parent[parent[num]]
                num = parent[num]
            return num

        def union(a, b):
            a = find(a)
            b = find(b)
            if rank[a] > rank[b]:
                parent[b] = a
            elif rank[b] > rank[a]:
                parent[a] = b
            else:
                parent[b] = a
                rank[a] += 1

        for i in range(n):
            a, b = points[i]
            for j in range(n):
                c, d = points[j]
                diff = abs(a-c) + abs(b-d)
                track[(i,j)] = diff
        nums = track.items()
        nums = sorted(nums, key = lambda x: x[1])
        for a, b in nums:
            if find(a[0]) != find(a[1]):
                result += b
                union(a[0], a[1])
        return result