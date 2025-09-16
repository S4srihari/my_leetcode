class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size()!= t.size()) return false;
        unordered_map<char,char> smap, tmap;
        for(int i=0; i <s.size(); i++){
            char c1 = s[i], c2 = t[i];
            if (smap.count(c1)) {
                if (smap[c1] != c2) return false;
            } 
            else if (tmap.count(c2)) {
                if (tmap[c2] != c1) return false;
            } 
            else {
                smap[c1] = c2;
                tmap[c2] = c1;
            }
        }
        return true;
    }
};