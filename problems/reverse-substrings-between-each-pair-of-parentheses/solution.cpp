class Solution {
public:
    string reverseParentheses(string s) {
       
        string stack;
      
        
        for (char& ch : s) {
            if (ch == ')') {
               
                string temp;
              
                
                while (stack.back() != '(') {
                    temp.push_back(stack.back());
                    stack.pop_back();
                }
              
                
                stack.pop_back();
              
                
                stack += temp;
            } else {
                
                stack.push_back(ch);
            }
        }
      
        // Return the final processed string
        return stack;
    }
};
