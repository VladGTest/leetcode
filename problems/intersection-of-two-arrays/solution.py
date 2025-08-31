class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sumsNums = []
        if(len(nums1) > len(nums2)):
            for i in range(len(nums1)):
                for j in range(len(nums2)):
                    if(nums1[i] == nums2[j] and nums1[i] not in sumsNums):
                        sumsNums.append(nums1[i])
        else:
             for i in range(len(nums2)):
                for j in range(len(nums1)):
                    if(nums2[i] == nums1[j] and nums2[i] not in sumsNums):
                        sumsNums.append(nums2[i])
        return sumsNums