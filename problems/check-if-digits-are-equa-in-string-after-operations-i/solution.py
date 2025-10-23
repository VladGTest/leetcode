class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        digits = list(map(int, s))
        n = len(digits)
        for k in range(n - 1, 1, -1):
            for i in range(k):
                digits[i] = (digits[i] + digits[i + 1]) % 10
        return digits[0] == digits[1]