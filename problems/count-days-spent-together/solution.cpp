class Solution {
public:
   
    vector<int> daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        
        string overlapStart = arriveAlice < arriveBob ? arriveBob : arriveAlice;
      
       
        string overlapEnd = leaveAlice < leaveBob ? leaveAlice : leaveBob;
      
        
        int startDay = convertDateToDayOfYear(overlapStart);
        int endDay = convertDateToDayOfYear(overlapEnd);
      
        
        return max(0, endDay - startDay + 1);
    }

private:
    
    int convertDateToDayOfYear(string dateString) {
        int month, day;
      
        
        sscanf(dateString.c_str(), "%d-%d", &month, &day);
      
        
        int totalDays = 0;
      
        
        for (int i = 0; i < month - 1; ++i) {
            totalDays += daysInMonth[i];
        }
      
        
        totalDays += day;
      
        return totalDays;
    }
};
