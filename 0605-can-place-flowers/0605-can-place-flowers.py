class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        for i in range(len(flowerbed)):
            if i == len(flowerbed)-1: 
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n-=1
                else: continue
            elif i == 0 and flowerbed[i+1] == 0 and flowerbed[0] == 0:
                flowerbed[0] = 1
                n-=1
            elif flowerbed[i] == 0:
                
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                   
                    flowerbed[i] = 1
                    n-=1
                 
        if n>0:
            return False
        else:
            return True
                