class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        unordered_set<char> broken(brokenLetters.begin(), brokenLetters.end());
        int count = 0;
        string word = "";

        for (int i = 0; i <= text.size(); i++) {
            if (i == text.size() || text[i] == ' ') {
                bool canType = true;
                for (char c : word) {
                    if (broken.count(c)) {
                        canType = false;
                        break;
                    }
                }
                if (canType && !word.empty()) count++;
                word.clear();
            } else {
                word.push_back(text[i]);
            }
        }
        return count;
        }
};