class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        track = defaultdict(int)
        total = 0
        result = 0
        left = 0
        
        for i in fruits:
            track[i] += 1
            total += 1
            
            while len(track) > 2:
                track[fruits[left]] -= 1
                
                if track[fruits[left]] == 0: track.pop(fruits[left])
                total -= 1
                left += 1
            
            result = max(result,total)

        return result
                