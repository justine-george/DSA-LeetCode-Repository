class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> result = new ArrayList<String>();
        
        Map<Integer, String> dict = new HashMap<>() {
            {
                put(3, "Fizz");
                put(5, "Buzz");
            }
        };
        
        for (int i = 1; i <= n; i++ ) {
            String ansStr = "";
            
            for (Integer key: dict.keySet()) {
                if (i % key == 0 ) {
                    ansStr += dict.get(key);
                }
            }
            
            if (ansStr.equals("")) {
                ansStr += Integer.toString(i);
            }
            
            result.add(ansStr);
        }
        return result;
    }
}