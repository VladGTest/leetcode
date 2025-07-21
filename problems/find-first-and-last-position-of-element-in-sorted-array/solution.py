class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arrSize = len(nums)

        first = -1
        last = -1

        for i in range(arrSize):
            if(target != nums[i]):
                continue
            
            if(first == -1):
                first = i
            
            last = i

        twoArr = [first, last]

        return twoArr
        