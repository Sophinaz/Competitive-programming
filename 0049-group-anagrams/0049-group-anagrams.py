from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagrams(strs):
            anagram = defaultdict(list)
            for i in range(len(strs)):
                sort_s = tuple(sorted(strs[i]))
                anagram[sort_s].append(strs[i])
            return anagram.values()
        return anagrams(strs)
        