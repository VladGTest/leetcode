class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int indexNumsOne = m - 1; 
        int indexNumsTwo = n - 1;
        int mergedIndex = m + n - 1;

        while (indexNumsTwo >= 0) {
            if (indexNumsOne < 0 || nums1[indexNumsOne] <= nums2[indexNumsTwo]) {
                nums1[mergedIndex] = nums2[indexNumsTwo]; 
                indexNumsTwo--;
            } else {
                nums1[mergedIndex] = nums1[indexNumsOne];
                indexNumsOne--;
            }
            mergedIndex--;

        }
    }
}