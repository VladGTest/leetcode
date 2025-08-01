class Solution {

    /**
     * @param Integer[][] $matrix
     * @return NULL
     */
    function rotate(&$matrix) {
        $n = count($matrix) - 1;
        $double_matrix = $matrix;
        for ($i = 0; $i < count($matrix);$i++){
            if(count($matrix) == count($matrix[$i])){
                $arr_index = 0;
                while ($arr_index <= $i){
                    for($j = 0; $j < count($matrix[$i]);$j++){
                        $temp = $double_matrix[$i][$j];
                        $matrix[$arr_index][$n] = $double_matrix[$i][$j];
                        $double_matrix[$i][$j] = $temp;
                        $arr_index++;
                    }
                }
                $n--;
            }
        }
    }
}