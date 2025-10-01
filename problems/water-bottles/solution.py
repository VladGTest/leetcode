class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int emptyBottles = 0 + numBottles;
        int sumDrinkBottles = 0 + numBottles;
        while(emptyBottles >= numExchange){
            int newBottles = emptyBottles / numExchange;
            sumDrinkBottles += newBottles;
            
            emptyBottles = emptyBottles % numExchange + newBottles;
        }
        return sumDrinkBottles;
    }
}