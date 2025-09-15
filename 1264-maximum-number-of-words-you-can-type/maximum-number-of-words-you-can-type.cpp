class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        int res = 0;
        unordered_set<char> broken(brokenLetters.begin(), brokenLetters.end());
        stringstream words(text);
        string word;
        while (words >> word){
            bool canType = true;
            for (char c : word){
                if (broken.count(c)){
                    canType = false;
                    break;
                }
            }
            if(canType) res++;
        }
        return res;
    }
};