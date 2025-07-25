class Solution {
    public void moveZeroes(int[] nums) {
        int indexZero = 0;
        for(int i = 0; i < nums.length;i++){
            if(nums[i] != 0){
                nums[indexZero] = nums[i];
                indexZero++;
            }
        }
        while(indexZero < nums.length){
            nums[indexZero] = 0;
            indexZero++;
        }
    }
}