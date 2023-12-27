class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def findthe(n,k):
            players = [playerNum+1 for playerNum in range(n)] 
            idx = 0 
            
            while len(players)>1:
                idx = (idx+k-1) % len(players) 
                players.pop(idx)
            return players[0] 
        return findthe(n,k)