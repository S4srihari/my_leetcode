class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill); m = len(mana)
        pref = [0]*n
        s = 0
        for i in range(n):
            s += skill[i]
            pref[i] = s

        S = [0]*m  
        for j in range(m-1):
            mx = 0
            for i in range(n):
                left  = mana[j] * pref[i]
                right = mana[j+1] * (pref[i-1] if i-1 >= 0 else 0)
                val = left - right
                if val > mx:
                    mx = val
            delta = mx if mx > 0 else 0
            S[j+1] = S[j] + delta

        finish = S[m-1] + mana[m-1] * pref[n-1]
        return finish