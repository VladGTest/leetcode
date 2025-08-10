class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map_array = {}

        for i in range(len(nums)):
            if (nums[i] in map_array and i - map_array[nums[i]] <= k):
                return True
            map_array[nums[i]] = i
            
        return False