class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal_triangle = [[1]]

        for i in range(1, numRows):
            new_row = [1]

            for j in range(1, i):
                new_row.append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i -1][j])
            new_row.append(1)

            pascal_triangle.append(new_row)


        return pascal_triangle

        
        
        