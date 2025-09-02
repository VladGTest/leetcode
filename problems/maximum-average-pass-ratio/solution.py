class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        classAverages = []
        averagePass = []
        sortedStudents = []
        for student in classes:
            classAverages[student] = [student[0], student[1]]
        
        for student in sorted(classAverages, key=classAverages.get, reverse=False):
            averagePass[student] = student[0] / student[1]
            sortedStudents[student] = [student[0], student[1]]
        
        for i in range(len(sortedStudents)):
            if(sortedStudent[i][0] / sortedStudent[i][1] == min(averagePass)):
                sortedStudent[i][0] = sortedStudent[i][0] + extraStudents
                sortedStudent[i][1] = sortedStudent[i][1] + extraStudents
                averagePass[0] = sortedStudent[i][0] / sortedStudent[i][1]
        
       return sum(averagePass) / len(classes)
        

