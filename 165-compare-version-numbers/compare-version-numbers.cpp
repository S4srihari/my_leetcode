class Solution {
public:
    int compareVersion(string version1, string version2) {
        vector<int> v1,v2;
        stringstream ss1(version1), ss2(version2);
        string s;
        while(getline(ss1,s,'.')){
            v1.push_back(stoi(s));
        }
        while(getline(ss2,s,'.')){
            v2.push_back(stoi(s));
        }
        int idx = 0, l1 =  v1.size(), l2 = v2.size();
        while(idx < l1 && idx < l2){
            if( v1[idx] > v2[idx]) return 1;
            else if (v1[idx] < v2[idx]) return -1;
            idx++;
        }
        while(idx < l1){
            if( v1[idx] > 0) return 1;
            idx++;
        }
        while(idx < l2){
            if (v2[idx] > 0) return -1;
            idx++;
        }
        return 0;
    }
};