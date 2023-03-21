class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        // int count =0;
        // int[] remArr = new int[60];
        // Arrays.fill(remArr,0);
        // for(int t: time){
        //     int r = t % 60;
        //     if(r == 0){
        //         remArr[0]++;
        //         count += remArr[0] - 1;
        //     } else if(remArr[60 - r] > 0){ // 1+59
        //         count += remArr[60 - r];
        //         remArr[r]++;
        //     } else{
        //         remArr[r]++;
        //     }
        // }
        // return count;
        
        
        int count = 0;
        int[] remArr = new int[60];
        for (int t : time) {
            int r = t % 60;
            int complement = (60 - r) % 60; // the complement of r
            count += remArr[complement];
            remArr[r]++;
        }
        return count;
    }
}
