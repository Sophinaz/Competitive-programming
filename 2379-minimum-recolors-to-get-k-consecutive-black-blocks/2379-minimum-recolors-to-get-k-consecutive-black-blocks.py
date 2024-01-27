class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l,r = 0,0
        pas,result = 0,len(blocks)+2
        while r<len(blocks):
            
            if blocks[r] == 'W':
                pas+=1
                r+=1
            else:
                r+=1
            if r-l == k:
                result = min(result, pas)
                if blocks[l] == 'W': pas -= 1
                l+=1
        return result