class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        unordered_set<string> store = {"X++", "++X"};
        int res = 0;
        for (string st: operations){
            if (store.count(st)) res++;
            else res--;
        }
        return res;
    }
};