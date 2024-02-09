class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        numWhite,numBlack = 0,0
        result = float('inf')
        
        left,right = 0,0
        
        while right < len(blocks):
            if blocks[right] == "W": numWhite += 1
            else: numBlack += 1

            if numBlack + numWhite > k:
                if blocks[left] == 'B': numBlack -= 1
                else: numWhite -= 1
                left += 1
            
            if numBlack + numWhite == k:
                result = min(result, numWhite)
            right += 1

        if result == float('inf'): return 0
        else: return result



