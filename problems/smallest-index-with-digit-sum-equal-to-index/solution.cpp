class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        
        for (int i = 0; i < nums.size(); ++i) {
            
            int digitSum = 0;
            int currentNumber = nums[i];
          
            
            while (currentNumber > 0) {
                digitSum += currentNumber % 10;  
                currentNumber /= 10;              
            }
          
            
            if (i % 10 == digitSum) {
                return i;
            }
        }
      
        
        return -1;
    }
};
