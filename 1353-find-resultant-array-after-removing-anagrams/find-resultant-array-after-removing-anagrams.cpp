class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
        vector<string> res;
        if (words.empty()) return res;
        res.push_back(words[0]);
        string prev = words[0];
        for (int i=1; i<words.size(); i++){
            string cur = words[i];
            int arr[26] = {0};
            for (char c:prev) arr[c-'a']++;
            for (char c:cur) arr[c-'a']--;
            bool valid = true;
            for (int f: arr){
                if (f != 0) {
                    valid = false;
                    break;
                }
            }
            if (!valid){ 
                res.push_back(cur);
                prev = cur;
            }
        }
        return res;
    }
};