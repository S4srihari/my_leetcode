class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int beams = 0, prevs = 0, lasers;
        for (int i=0; i<bank.size(); i++){
            lasers = 0;
            for (char c : bank[i]){
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