class Solution {
public:
    int minMoves(vector<int>& nums) {
        int maxElement = *std::max_element(begin(nums), end(nums));
        int counterToEquel = 0;
        for(int i = 0; i < nums.size();i++){
            int temp = nums[i];
            while(temp < maxElement){
                counterToEquel++;
                temp++;
            }
        }
        return counterToEquel;
    }
};