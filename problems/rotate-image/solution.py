from copy import deepcopy

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        double_matrix = deepcopy(matrix)
        for i in range(len(matrix)):
            if(len(matrix) == len(matrix[i])):
                arr_index = 0
                while (arr_index <= i):
                    for j in range(len(matrix[i])):
                        temp = double_matrix[i][j]
                        matrix[arr_index][n] = double_matrix[i][j]
                        double_matrix[i][j] = temp
                        arr_index+=1
                n-=1    
                
                
            
        
        