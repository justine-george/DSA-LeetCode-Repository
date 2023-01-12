class Solution {
    public List<String> generatePossibleNextMoves(String currentState) {
        HashSet<String> result = new HashSet<>();
        char[] curr = currentState.toCharArray();
        char[] temp;
        for (int i = 0; i < curr.length - 1; i++) {
            if (curr[i] == '+' && curr[i+1] == '+') {
                temp = Arrays.copyOf(curr, curr.length);
                temp[i] = temp[i+1] = '-';
                result.add(String.valueOf(temp));
            }
        }
        return new ArrayList<String>(result);
    }
}