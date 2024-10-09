class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        length = max(len(word) for word in words)
        result = [[] for i in range(length)]
        print(result)

        for i in range(len(words)):
            for j in range(length):
                if j < len(words[i]):
                    result[j%length].append(words[i][j])
                else:
                    result[j%length].append(' ')
        return [''.join(i).rstrip() for i in result]