class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        track = {}
        stack = []
        answer = [-1] * len(nums1)

        for i in nums2:
            if not stack: stack.append(i)

            if i > stack[-1]: 
                while stack and i > stack[-1]:
                    x = stack.pop()
                    track[x] = i
                stack.append(i)
            
            if stack and i < stack[-1]:
                stack.append(i)

        for i in range(len(nums1)):
            answer[i] = track.get(nums1[i],-1)
        return answer