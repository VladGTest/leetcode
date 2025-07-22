class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        for i in range(0, len(num)):
            num = num ^ nums[i]
        return num
        