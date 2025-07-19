class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        isNext = False
        counter = len(digits)
        for i in range(counter - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10

            if(digits[i] != 0):
                return digits
        
        return [1] + digits
            
            
            
            

        