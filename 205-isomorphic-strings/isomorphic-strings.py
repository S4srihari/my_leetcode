class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """s_hash = defaultdict(int)
        t_hash = defaultdict(int)
        for idx in range(len(s)):
            if s[idx] not in s_hash:
                s_hash[s[idx]] = idx
            
            if t[idx] not in t_hash:
                t_hash[t[idx]] = idx
            
            if s_hash[s[idx]] != t_hash[t[idx]]:
                return False
        return True"""

        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))