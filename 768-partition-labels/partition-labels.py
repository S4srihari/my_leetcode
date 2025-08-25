class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        hash_map = {}
        for i in range(len(s)):
            hash_map[s[i]] = i
        right = hash_map[s[0]]
        start = 0
        for idx in range(len(s)):
            if idx == right:
                res.append(idx-start+1)
                start = idx+1
                if idx < len(s)-1 :
                    right = hash_map[s[idx+1]] 
            else: 
                right = max(right,hash_map[s[idx]])
        return res