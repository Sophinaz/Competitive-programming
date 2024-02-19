class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        answer = [-1] * n
        for idx in range(2*n):
            i = idx % n
            if not stack: 
                stack.append(i)
                continue
            

            while stack and nums[i] > nums[stack[-1]]:
                x = stack.pop()
                answer[x] = nums[i]
            stack.append(i)
            

        return answer


