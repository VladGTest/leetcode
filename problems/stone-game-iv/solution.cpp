class Solution {
public:
    bool winnerSquareGame(int n) {
        int dp[n + 1];
        memset(dp, 0, sizeof(dp));
        function<bool(int)> canWin = [&](int remainingStones) -> bool {
            if (remainingStones <= 0) {
                return false;
            }
          
            if (dp[remainingStones] != 0) {
                return dp[remainingStones] == 1;
            }
          
            for (int k = 1; k * k <= remainingStones; ++k) {
                if (!canWin(remainingStones - k * k)) {
                    dp[remainingStones] = 1; 
                    return true;
                }
            }
          
          
            dp[remainingStones] = -1; 
            return false;
        };
        return canWin(n);
    }
};