class Solution:
    def splitString(self, s: str) -> bool:
        nums = []
        def split(idx):
            if idx >= len(s):

                return len(nums) >= 2

            for i in range(idx,len(s)):
                val = int(s[idx:i+1])
                if (nums and nums[-1] - val == 1) or (not nums): 
                    nums.append(val)
                    if split(i+1): return True
                    nums.pop()

            return False
        return split(0)