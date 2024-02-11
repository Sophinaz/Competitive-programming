class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key = lambda x: x[2])
        n = trips[len(trips)-1][2]
        answer = [0] * (n+2)

        for a,b,c in trips:
            answer[b] += a
            answer [c] -= a

        for i in range(1,len(answer)):
            answer[i] = answer[i-1] + answer[i]

        if max(answer) > capacity : return False
        else: return True