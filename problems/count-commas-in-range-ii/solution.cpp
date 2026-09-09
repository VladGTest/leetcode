class Solution {
public:
    long long countCommas(long long n) {
        long long sum = 0;
        for(long long i = 1000; i <= n; i *= 1000)
        {
            sum += n - i + 1;
        }
        return sum;
    }
};