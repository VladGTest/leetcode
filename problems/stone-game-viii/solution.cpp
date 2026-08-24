class Solution {
public:
    int stoneGameVIII(vector<int>& stones) {
        int n = stones.size();
    
        for (int i = 1; i < n; ++i) {
            stones[i] += stones[i - 1];
        }
      
        int dp[n];
        memset(dp, -1, sizeof(dp));
    
        function<int(int)> dfs = [&](int index) -> int {
    
            if (index >= n - 1) {
                return stones[index];
            }
          
           
            if (dp[index] == -1) {
                int skipCurrent = dfs(index + 1);
                int takeCurrent = stones[index] - dfs(index + 1);
              
                dp[index] = max(skipCurrent, takeCurrent);
            }
          
            return dp[index];
        };
        return dfs(1);
    }
};
