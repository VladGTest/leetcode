class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing_num = 0
        l = len(nums) + 1
        
        for i in range(l):
            missing_num ^= i
            if i < l - 1:
                missing_num ^= nums[i]    
                
        return missing_num
        