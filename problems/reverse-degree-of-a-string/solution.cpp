class Solution {
public:
    int reverseDegree(string s) {
        int stringLength = s.length();
        int totalReverseDegree = 0;
        for (int position = 1; position <= stringLength; ++position) {
            char currentChar = s[position - 1];
          
            int reverseAlphabeticalValue = 26 - (currentChar - 'a');
            totalReverseDegree += position * reverseAlphabeticalValue;
        }
      
        return totalReverseDegree;
    }
};
