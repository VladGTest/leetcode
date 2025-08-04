class Solution {

    static int[] shuffleArray(int[] ar)
    {
        Random rnd = new Random();
        for (int i = ar.length - 1; i > 0; i--)
        {
            int index = rnd.nextInt(i + 1);
            int a = ar[index];
            ar[index] = ar[i];
            ar[i] = a;
        }
        return ar;
    }

    

    public static int[][] addArray(int[][] array, int[] addArray){
        int[][] newArray = new int[array.length + 1][];
        for(int i = 0; i < array.length;i++){
            newArray[i] = array[i];
        }
        newArray[newArray.length - 1] = addArray;
        return newArray;
    }

    public List<List<Integer>> permute(int[] nums) {
        int count = (nums.length * 2) - 1;
        int[][] sumArr = new int[][]{};
        sumArr = addArray(sumArr, nums);
        ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
        list.add(Arrays.asList(nums));
        boolean isUnique = false;

        for(int i = 0; i < count;i++){
            isUnique = true;
            int[] tempArr = shuffleArray(nums);
            for(int j = 0; j < sumArr.length;j++){
                if(tempArr == sumArr[j]){
                    isUnique = false;
                }
            }
            if(isUnique){
                list.add(Arrays.asList(tempArr));
                i++;
            }
            i--;
        }
        //List<List<Integer>> list = Arrays.asList(sumArr);
        return list;
    }
}
