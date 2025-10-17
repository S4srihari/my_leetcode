class Solution {
public:
    int minSteps(string s, string t) {
        int arr[26] = {0};
        for (char c: s) arr[c-'a']++;
        for (char c: t) arr[c-'a']--;
        int res =0;
        for (int i=0; i<26; i++) res += std::abs(arr[i]);
        return res;
    }
};