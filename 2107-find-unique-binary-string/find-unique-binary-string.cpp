class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        string res = "";
        for (int i = 0; i < size(nums[0]); i++) {
            if (nums[i][i] == '0') {
                res += '1';
            } else {
                res += '0';
            }
        }
        return res;
    }
};