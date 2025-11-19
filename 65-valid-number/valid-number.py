class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)
        if n == 1 and not s[0].isdigit(): return False
        e_idx = n
        s = s.lower().strip()
        e_cnt = s.count('e')
        if e_cnt > 1: return False
        elif e_cnt == 1:
            e_idx = s.index('e')
            if e_idx == 0: return False
        if e_idx != n:
            if e_idx + 1 == n: return False
            if s[e_idx+1] not in ('+', '-') and not s[e_idx+1].isdigit():
                return False
            if s[e_idx+1] in ('+', '-') and e_idx + 2 == n: return False
            for c in range(e_idx+2,n):
                if not s[c].isdigit(): return False
        
        dot_idx = n
        dot_cnt = s.count('.')
        if dot_cnt > 1: return False
        elif dot_cnt == 1: 
            dot_idx = s.index('.')
        if dot_idx < n:
            for i in range(dot_idx+1, e_idx):
                if not s[i].isdigit(): return False
        
        if s[0] != '.' and s[0] not in ('+', '-') and not s[0].isdigit():
            return False
        if e_idx < n and dot_idx < n :
            if dot_idx + 1 == e_idx:
                if dot_idx == 0: return False
                elif dot_idx == 1 and not s[0].isdigit(): return False
            for i in range(1,dot_idx):
                if not s[i].isdigit(): return False
        elif e_idx < n:
            if e_idx == 1 and not s[0].isdigit(): return False 
            for i in range(1,e_idx):
                if not s[i].isdigit(): return False
        elif dot_idx < n:
            if dot_idx == 1 and not s[0].isdigit() and e_idx == 2: 
                return False
            for i in range(1,dot_idx):
                if not s[i].isdigit(): return False
        else:
            for i in range(1,n):
                if not s[i].isdigit(): return False
        return True

        