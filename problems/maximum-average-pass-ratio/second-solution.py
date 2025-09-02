class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        heap = []
        
        for passed, total in classes:
            
            current_ratio = passed / float(total)
            new_ratio = (passed + 1) / float(total + 1)
            improvement = new_ratio - current_ratio
            
            heapq.heappush(heap, (-improvement, passed, total))
        
       
        for _ in range(extraStudents):
           
            neg_improvement, passed, total = heapq.heappop(heap)
            
           
            passed += 1
            total += 1
            
            
            current_ratio = passed / float(total)
            new_ratio = (passed + 1) / float(total + 1)
            improvement = new_ratio - current_ratio
            
            
            heapq.heappush(heap, (-improvement, passed, total))
        
        
        total_ratio = 0.0
        for neg_improvement, passed, total in heap:
            total_ratio += passed / float(total)
        
        return total_ratio / len(classes)
        

