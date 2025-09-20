class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_map<char,int> sHash, tHash;
        for (int i = 0; i<s.size(); i++){
            sHash[s[i]]++;
            tHash[t[i]]++;
        }
        return sHash == tHash;
    }
};