class Solution {
public:
    int maxFreqSum(string s) {
        int freq[26] = {0};
        for(char c: s){
            freq[c-'a'] += 1;
        }
        int vowels[5] = {0,4,8,14,20};
        int maxVowel = 0;
        for (int i : vowels){
            if (freq[i] > maxVowel){
                maxVowel = freq[i];
            }
            freq[i] = 0;
        }
        int maxCons = 0;
        for(int i : freq){
            if (i > maxCons) maxCons = i; 
        }
        return maxVowel + maxCons;
    }
};