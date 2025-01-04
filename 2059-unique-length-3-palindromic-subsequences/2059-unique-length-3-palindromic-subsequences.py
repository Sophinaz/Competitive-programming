class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        positions = defaultdict(list)
        result = 0
        for i in range(len(s)):
            if s[i] not in positions:
                positions[s[i]] = [i,i]
            else:
                positions[s[i]][0] = min(positions[s[i]][0], i)
                positions[s[i]][1] = max(positions[s[i]][1], i)

        for letter in positions:
            check = set()
            for i in range(positions[letter][0] + 1, positions[letter][1]):
                check.add(s[i])
            result += len(check)

        return result