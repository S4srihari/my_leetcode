class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """l = s.split(" ")
        if len(pattern) != len(l):
            return False
        return len(set(pattern)) == len(set(l)) == len(set(zip(pattern,l)))"""

        l = s.split(" ")
        if len(pattern) != len(l):
            return False
        
        l_hash = defaultdict(int)
        p_hash = defaultdict(int)
        for idx in range(len(pattern)):
            if pattern[idx] not in p_hash:
                p_hash[pattern[idx]] = idx
            if l[idx] not in l_hash:
                l_hash[l[idx]] = idx
            
            if p_hash[pattern[idx]] != l_hash[l[idx]]:
                return False
            
        return True