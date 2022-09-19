class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> result = new ArrayList<String>();
        for (int i = 1; i <= n; i++ ) {
            boolean div3 = i % 3 == 0;
            boolean div5 = i % 5 == 0;
            String ansStr = "";
            
            if (div3) {
                ansStr += "Fizz";
            }
            if (div5) {
                ansStr += "Buzz";
            }
            if (ansStr.equals("")) {
                ansStr += Integer.toString(i);
            }
            
            result.add(ansStr);
        }
        return result;
    }
}