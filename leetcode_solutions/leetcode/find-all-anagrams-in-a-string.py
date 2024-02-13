class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []
        countp = {}
        counts = {}
        result = []
        left = 0
        for i in p:
            if i not in countp: countp[i] = 1
            else: countp[i] += 1
        for i in range(len(p)):
            if s[i] not in counts: counts[s[i]] = 1
            else: counts[s[i]] += 1
        if counts == countp: result.append(left)
        for i in range(len(p),len(s)):
            if s[i] not in counts: counts[s[i]] = 1
            else: counts[s[i]] += 1

            counts[s[left]] -= 1

            if counts[s[left]] == 0: counts.pop(s[left])
            left +=1

            if counts == countp:
                result.append(left)
        return result