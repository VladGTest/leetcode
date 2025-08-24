class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestSubarray($nums) {
        $left = 0;
        $zeros = 0;
        $maxLength = 0;
        $n = count($nums);
        
        for ($right = 0; $right < $n; $right++) {
            if ($nums[$right] == 0) {
                $zeros++;
            }
        
            while ($zeros > 1) {
                if ($nums[$left] == 0) {
                    $zeros--;
                }
                $left++;
            }
        
            $maxLength = max($maxLength, $right - $left);
        }
        
        return $maxLength;
    }
}