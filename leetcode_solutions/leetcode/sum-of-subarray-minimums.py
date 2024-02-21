class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        nums= arr
        n = len(arr)
        stack = []
        right = [-1] * n
        left = [-1] * n
        result = 0
        for i in range(n):
            if not stack:
                stack.append(i)
                continue
            if nums[i] <= nums[stack[-1]]:
                while stack and  nums[i] <= nums[stack[-1]]:
                    x = stack.pop()
                    right[x] = i-x
                stack.append(i)
            if nums[i] >= nums[stack[-1]]:
                stack.append(i)
        stack = []
        for i in range(n-1,-1,-1):
            if not stack:
                stack.append(i)
                continue
            if nums[i] < nums[stack[-1]]:
                while stack and  nums[i] < nums[stack[-1]]:
                    x = stack.pop()
                    left[x] = x - i
                stack.append(i)
            if nums[i] >= nums[stack[-1]]:
                stack.append(i)

        for i in range(n):
            x = right[i]
            y = left[i]
            if x == -1: x = n - i
            if y == -1: y = i+1
            result += (x*y*nums[i])

        return result % ((10 ** 9)+7)



        