/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let k = nums.length;
    for(let i = 0; i < k;i++){
       if(i < nums.length){
            if(nums[i] === nums[i + 1]){
                nums.splice(i, 1);
                i--;
            }
       }
    }
    return k;
};