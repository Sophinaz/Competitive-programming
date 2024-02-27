class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def comb(num,path):
            if len(path) == k: 
                answer.append(path)
                return

            for i in range(num+1,n+1):
                path.append(i)
                comb(i,path[:])               
                path.pop()

            return answer
        return comb(0,[])
