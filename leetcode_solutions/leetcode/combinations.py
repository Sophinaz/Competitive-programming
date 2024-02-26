class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        path = []
        def comb(num):
            if len(path) == k: 
                answer.append(path.copy())
                return

            for i in range(num+1,n+1):
                path.append(i)
                
                comb(i)
                
                path.pop()

            return answer
        return comb(0)
