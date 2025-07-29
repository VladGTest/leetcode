class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalSum = 0
        element = None

        for num in nums:
            if totalSum == 0:
                element = num
                count = 1
            elif element == num:
                totalSum += 1
            else:
                totalSum -= 1
        return element
        