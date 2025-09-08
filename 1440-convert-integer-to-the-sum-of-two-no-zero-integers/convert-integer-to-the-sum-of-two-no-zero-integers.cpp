class Solution {
public:
    bool check(int x){
            while(x > 0){
                int mod = x%10;
                if(mod == 0) return true;
                x = x/10;
            }
            return false;
        }

    vector<int> getNoZeroIntegers(int n) {
        for(int a=1;a<n;a++){
            if(!check(a) && !check(n-a)){
                return {a,n-a};
            }
        }
        return {};
    }
};