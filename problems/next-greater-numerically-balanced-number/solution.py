class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        for candidate in count(n + 1):
            digit_count = [0] * 10
            temp_num = candidate
            while temp_num > 0:
                temp_num, digit = divmod(temp_num, 10)
                digit_count[digit] += 1

            is_beautiful = all(
                count == 0 or digit == count 
                for digit, count in enumerate(digit_count)
            )

            if is_beautiful:
                return candidate