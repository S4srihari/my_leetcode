class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> hash;
        for (string str : strs ){
            string anag = str;
            sort(str.begin(),str.end());
            hash[str].push_back(anag);
        }
        vector<vector<string>> res;
        for (auto pair : hash){
            res.push_back(pair.second);
        }
        return res;
    }
};