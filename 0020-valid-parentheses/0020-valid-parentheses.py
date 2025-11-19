class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in check:
                if stack and stack.pop() == check[char]:
                    continue
                return False
            else:
                stack.append(char)

        return True