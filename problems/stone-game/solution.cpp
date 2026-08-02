class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        int n = piles.size();

        vector<vector<int>> dp(n, vector<int>(n, 0));

    
        for (int i = 0; i < n; i++) {
            dp[i][i] = piles[i];
        }

        for (int length = 2; length <= n; length++) {
            for (int left = 0; left + length <= n; left++) {
                int right = left + length - 1;

                int takeLeft = piles[left] - dp[left + 1][right];
                int takeRight = piles[right] - dp[left][right - 1];

                dp[left][right] = max(takeLeft, takeRight);
            }
        }

        return dp[0][n - 1] > 0;
    }
};