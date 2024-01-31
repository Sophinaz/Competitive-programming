class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def closestElements(arr,k,x):
            track = {}
            result = []
            for i in arr:
                if i not in track: track[i] = [abs(i-x),1]
                else: track[i][1] +=1
            combined = track.items()
            combined = sorted(combined, key = lambda x: x[1][0])
            for i,j in combined:
                for _ in range(j[1]):
                    if len(result) < k:
                        result.append(i)
            result = sorted(result)
            return result
        return closestElements(arr,k,x)