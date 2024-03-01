class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        numsa = firstList
        numsb = secondList
        result = []
        left,right = 0,0
        
        while left< len(numsa) and right < len(numsb):
            
            if numsb[right][0] <= numsa[left][0] <= numsb[right][1]:
                minn = min(numsa[left][1], numsb[right][1])
                result.append([numsa[left][0], minn])

            elif numsa[left][0] <= numsb[right][0] <= numsa[left][1]:
                minn = min(numsb[right][1], numsa[left][1])
                result.append([numsb[right][0], minn])
            
            if numsa[left][1] < numsb[right][1]:
                left += 1
            else: right += 1
        return result
