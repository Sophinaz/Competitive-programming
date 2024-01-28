class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        outside = []
        inside = []
        for i in arr1:
            if i in arr2: inside.append(i)
            else: outside.append(i)
        c = Counter(inside)
        ins = []
        for i in range(len(arr2)):
            for j in range(c[arr2[i]]):
                ins.append(arr2[i])
        return ins + sorted(outside)
