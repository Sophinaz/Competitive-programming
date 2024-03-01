class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k1 = k
        nums = []
        while k1 >1: 
            nums.append(k1)
            k1 = math.ceil(k1/2) 
        answer = 0

        def backtrack(curr, score, n):
            nonlocal answer
            if n == 0: return
            if score == k:
                answer = curr
                return
                        
            if curr == 0:
                if score * 2 == nums[-1]:
                    nums.pop()
                    backtrack(1, (score * 2), n-1)
                else:
                    nums.pop()
                    backtrack(0, (score * 2)-1, n-1)
            
            else:
                if score * 2 == nums[-1]:
                    nums.pop()
                    backtrack(0, (score * 2), n-1)
                else:
                    nums.pop()
                    backtrack(1, (score * 2)-1, n-1)

        backtrack(0,1,n)
        return answer
