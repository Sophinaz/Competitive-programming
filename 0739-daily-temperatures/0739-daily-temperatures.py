class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        track = {}
        stack = []
        n = len(temperatures)
        nums = temperatures
        answer = [0] * n
        idx = 0

        for i in range(n):
            if not stack: 
                stack.append(nums[i])
                idx = i
                continue

            if nums[i] > stack[-1]: 
                while stack and nums[i] > stack[-1]:
                    x = stack.pop()
                    answer[idx] = i -idx
                    while answer[idx] != 0: idx -= 1
                stack.append(nums[i])
                idx = i
            
            elif stack and nums[i] <= stack[-1]:
                stack.append(nums[i])
                idx = i

        return answer