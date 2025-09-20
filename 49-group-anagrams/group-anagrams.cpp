class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> hash;
        for (string str : strs ){
            vector<int> freq(26,0);
            for (char c : str){ freq[c-'a']++;}
            string key = to_string(freq[0]);
            for (int i = 1; i < 26; i++){
                key += ',' + to_string(freq[i]);
            }
            hash[key].push_back(str);
        }
        vector<vector<string>> res;
        for (auto pair : hash){
            res.push_back(pair.second);
        }
        return res;
    }
};