class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s += str(i)

        s1 = str(int(s)+1)
        nums = [0] * len(s1)
        for i in range(len(s1)): nums[i] = int(s1[i])
        return nums
