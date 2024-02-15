class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        result = 0
        while target > 1:
            if maxDoubles == 0:
                result += target - 1
                break
            
            if target % 2 == 0 and maxDoubles > 0:
                target = target // 2
                result += 1
                maxDoubles -= 1

            else:
                target -= 1
                result += 1
        return result
        
         
        

