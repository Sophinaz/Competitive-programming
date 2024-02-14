class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = 0
        t = 0
        for i in nums:
            if i != val:
                nums[n] = i
                n += 1
            else:
                t+=1
        for j in range(t):
            nums.pop()
            
        
        print(n, nums)