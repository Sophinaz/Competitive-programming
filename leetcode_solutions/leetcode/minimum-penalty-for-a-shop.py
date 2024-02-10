class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penality = customers.count('Y')
        track = {penality : 0}
        for i in range(len(customers)):
            if customers[i] == 'Y':
                penality -= 1
                
            else: penality += 1
            
            if penality not in track:
                track[penality] = i+1
        k = min(track)
        return track[k]