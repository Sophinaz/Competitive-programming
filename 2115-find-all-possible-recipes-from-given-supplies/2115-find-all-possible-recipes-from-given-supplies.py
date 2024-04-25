class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        check = set(recipes)
        graph = defaultdict(list)
        income = defaultdict(int)
        result = []
        for i in range(n):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                income[recipes[i]] += 1
    
        que = deque(supplies)
        
        while que:
            node = que.popleft()
            for child in graph[node]:
                income[child] -= 1
                if income[child] == 0:
                    if child in check:
                        result.append(child)
                    que.append(child)
        
        return result

        
