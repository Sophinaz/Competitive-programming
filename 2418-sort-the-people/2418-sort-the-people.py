class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined = zip(names,heights)
        combined = sorted(combined,key = lambda x: x[1],reverse =True )
        result = []
        for i,j in combined: result.append(i)
        return result