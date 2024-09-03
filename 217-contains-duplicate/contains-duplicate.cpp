class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> visited;
        for (const auto& num: nums) {
            if (visited.count(num)) {
                return true;
            }
            visited.insert(num);
        }
        return false;
    }
};