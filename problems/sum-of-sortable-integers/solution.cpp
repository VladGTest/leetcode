class Solution {
public:
    pair<int,int> sortable(vector<int>& nums, int a, int b){
        int idx_max = -1;
        int mx = -1; 
        for(int i = a; i <= b; i++){
            if(nums[i] >= mx){
                mx = nums[i];
                idx_max = i;
            }
        }
        
        int up = ((idx_max+1-a)%(b-a+1))+a;
        if(idx_max == b && nums[up] ==  mx){
            up++;
        }
        for(int i = 0; i < b-a; i++){
            if(nums[((up+i-a)%(b-a+1))+a] > nums[((up+i+1-a)%(b-a+1))+a]){
                return {-1,-1};
            }
        }
        return {nums[up],mx};
        
    }
    int sortableIntegers(vector<int>& nums) {
        int res = 0;
        if(is_sorted(nums.begin(), nums.end())){
            res += 1;
        }
        for(int i = 2; i <= nums.size(); i++){
           
            if(nums.size() % i == 0){
                int last = 0; 
                int d = nums.size() / i ;
                bool var = true; 
                for(int j = 0; j < d; j++){
                    auto [mn, mx] = sortable(nums,j*i,j*i+i-1);
                    
                    if(mn >= last){
                        last = mx; 
                    }
                    else{
                        var = false;
                        break;
                    }
                }
                
                if(var){
                    res += i; 
                }
            }
        }
        return res;
    }
};