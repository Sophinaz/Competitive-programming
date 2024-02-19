class Solution:
    def isValid(self, s: str) -> bool:
        tracker = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if stack and i in tracker:
                if stack[-1] == tracker[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack: return False
        return True
