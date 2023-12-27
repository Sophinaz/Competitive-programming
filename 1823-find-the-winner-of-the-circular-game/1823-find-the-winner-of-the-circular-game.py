class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def findthe(n,k):
            arr = deque(list(range(1,n+1)))
            while len(arr) > 1:
                c = k-1
                while c > 0:
                    arr.append(arr.popleft())
                    c-=1

                arr.popleft()
            return arr[0]
        return findthe(n,k)


        