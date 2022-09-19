class Solution {
    public int numberOfSteps(int num) {
        int counter = 0;
        if (num <= 0) return 0;
        while(num > 0) {
           if ((num & 1) == 1)
               counter+=2;
            else {
                counter++;
            }
            num = num >> 1;
        }
        return counter-1;
    }
}