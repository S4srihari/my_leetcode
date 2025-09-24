class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        string sign = "";
        if (numerator == 0) return "0";
        if ((numerator < 0)^(denominator < 0)) sign = "-";
        long long numer = abs((long long)numerator), denom = abs((long long)denominator);
        stringstream ss;
        long long q = numer / denom;
        ss << q;
        if (q*denom == numer) return sign + ss.str();
        ss << "."; numer %= denom;
        int pos = 1;
        unordered_map<int, int> hash;
        while(true){
            if (hash.count(numer)) break;
            hash[numer] = pos; pos++;
            numer *= 10;
            q = numer/denom;
            ss << q;
            if (q * denom == numer) return sign + ss.str();
            if (numer >= denom) numer %= denom; 
        }
        string res = ss.str();
        int len = res.size();
        int inlen = pos-hash[numer];
        return sign + res.substr(0,len-inlen) + "(" + res.substr(len-inlen, inlen) + ")";
    }
};