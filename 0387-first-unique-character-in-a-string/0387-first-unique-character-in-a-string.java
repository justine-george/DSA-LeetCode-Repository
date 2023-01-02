class Solution {
    public int firstUniqChar(String s) {
        int[] bmap = new int[26];
        // form bitmap
        for (char c: s.toCharArray()) {
            bmap[c-'a']++;
        }
        int index = 0;
        // find index of first unique character
        for (char c: s.toCharArray()) {
            if (bmap[c-'a'] == 1) {
                return index;
            }
            index++;
        }
        // character not found, return zero
        return -1;
    }
}