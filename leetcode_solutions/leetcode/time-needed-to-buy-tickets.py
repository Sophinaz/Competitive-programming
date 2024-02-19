class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        line = deque(tickets)
        value = line[k]
        time = 0
        while value > 0:
            time += 1
            x = line.popleft()
            if x != 1: line.append(x-1)
            k-=1
            if k == -1: 
                k = len(line)-1
                value -= 1

        return time
