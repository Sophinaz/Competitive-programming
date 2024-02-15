class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        track = {}
        result = 0

        for i in answers:
            if i not in track and i != 0:
                track[i] = i
                result += i+1
            elif i == 0: result += 1
            
            else: 
                track[i] -= 1
                if track[i] == 0: track.pop(i)

        return result

            

