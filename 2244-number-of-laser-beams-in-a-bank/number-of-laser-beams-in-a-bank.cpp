class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int beams = 0, prevs = 0, lasers;
        for (string row : bank){
            lasers = 0;
            for (char c : row){
                if (c == '1') lasers++;
            }
            if (lasers > 0){
                beams += prevs*lasers;
                prevs = lasers;
            }
        }
        return beams;
    }
};