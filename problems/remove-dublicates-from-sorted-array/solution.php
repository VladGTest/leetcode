class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function removeDuplicates(&$nums) {
        $k = count($nums);
        for($i = 0; $i < $k;$i++){
            if($i < count($nums)){
                if($nums[$i] == $nums[$i + 1]){
                    array_splice($nums, $i, 1);
                    $i--;
                }
            }
        }
        return $k;
    }
}