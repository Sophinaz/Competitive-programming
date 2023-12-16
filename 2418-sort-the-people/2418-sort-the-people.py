class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def people(names,heights):
            hashe = dict(zip(heights,names))
            heights.sort(reverse=True)
            ans = []
            for i in heights:
                ans.append(hashe[i])
            return ans
        return people(names,heights)
        