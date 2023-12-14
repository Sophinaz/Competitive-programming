class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagrams(strs):
            anagram = {}
            for i in range(len(strs)):
                if tuple(sorted(strs[i])) in anagram.keys():
                    anagram[tuple(sorted(strs[i]))].append(strs[i])
                else:
                    anagram[tuple(sorted(strs[i]))] = [strs[i]] 
                
            return anagram.values()
        return anagrams(strs)
        