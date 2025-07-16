/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let numsSum = nums1.concat(nums2);

    if(numsSum.length === 1){
        return numsSum[0];
    }

    numsSum.sort(function (a, b) {
        return a - b;
    });

    let avarageLength = Math.floor(numsSum.length / 2);

    if(numsSum.length % 2 !== 0){
        return numsSum[avarageLength];
    }else{
        return (numsSum[avarageLength - 1] + numsSum[avarageLength]) / 2;
    }
    
};