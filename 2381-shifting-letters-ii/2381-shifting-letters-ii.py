class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_val = [0 for i in range(len(s))]
        result = []

        for a, b, c in shifts:
            if c == 1:
                shift_val[a] += 1
                if b < len(s) - 1:
                    shift_val[b+1] -= 1
            else:
                shift_val[a] -= 1
                if b < len(s) - 1:
                    shift_val[b+1] += 1
        
        for i in range(1, len(s)):
            shift_val[i] += shift_val[i-1]

        for idx in range(len(s)):
            result.append(chr(((ord(s[idx]) - ord('a') + shift_val[idx]) % 26) + ord('a')))

        return ''.join(result)