class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        max_diag = 0
        max_area = 0
        
        for rect in dimensions:
            length, width = rect
            
            diag_sq = length * length + width * width
            area = length * width
            
            if diag_sq > max_diag:
                max_diag = diag_sq
                max_area = area
    
            elif diag_sq == max_diag:
                
                if area > max_area:
                    max_area = area
        
        return max_area
        