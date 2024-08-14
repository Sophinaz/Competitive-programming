class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        final = []
        for num in range(len(nums)):
            number = ""
            for i in str(nums[num]):
                number += str(mapping[int(i)])
            x = int(number)
            final.append([x, num])

        final.sort()
        answer = []
        for a, b in final:
            answer.append(nums[b])
        return answer