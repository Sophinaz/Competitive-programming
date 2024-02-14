class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        r = len(arr)
        result = []
        while r > 1:
            num = arr.index(r)
         
            if num == r-1:
                r-=1
                continue
            if num != 0:
                arr[:num+1] = reversed(arr[:num+1])
                result.append(num+1)
            arr[:r] = reversed(arr[:r])
            result.append(r)
            r-=1
        return result