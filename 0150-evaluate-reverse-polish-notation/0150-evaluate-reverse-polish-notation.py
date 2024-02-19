class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+' and stack:
                y = stack.pop()
                if stack: x = stack.pop()
                stack.append(x+y)
            elif i == '*' and stack:
                y = stack.pop()
                if stack: x = stack.pop()
                stack.append(x*y) 
            elif i == '/' and stack:
                y = stack.pop()
                if stack: x = stack.pop()
                ans = x//y
                if ans <0 and x % y != 0: ans += 1
                stack.append(ans)
            elif i == '-' and stack:
                y = stack.pop()
                if stack: x = stack.pop()
                stack.append(x-y)
            else:
                stack.append(int(i))
        if stack: return stack[0]
        else: return -1