class Solution {
    public int firstUniqChar(String s) {
        int[] letter = new int[26];
        // form counter map
        for (char c: s.toCharArray()) {
            letter[c-'a']++;
        }
        
        int index = 0;
        // find index of first unique character
        for (char c: s.toCharArray()) {
            if (letter[c-'a'] == 1) {
                return index;
            }
            index++;
        }

        // character not found, return zero
        return -1;
    }
}