class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int> hash;
        for (int i : nums){
            hash[i]++;
        } 
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        for (auto pair: hash){
            pq.push({pair.second,pair.first});
            if (pq.size() > k) pq.pop();
        }
        vector<int> res;
        while(!pq.empty()){
            res.push_back(pq.top().second);
            pq.pop();
        }
        return res;  
    }
};