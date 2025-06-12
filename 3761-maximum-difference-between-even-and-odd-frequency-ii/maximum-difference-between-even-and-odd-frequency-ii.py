class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        mxDiff = -inf

        prefs = defaultdict(lambda: [0] * len(s))
        for i, ch in enumerate(s): prefs[ch][i] = 1

        for ch in prefs:
            prefs[ch] = list(accumulate(prefs[ch], initial = 0))    

        for a, b in permutations(prefs, 2):
            if not(a in s and b in s): continue

            abPrefs = list(zip(prefs[a], prefs[b]))
            
            diff = {(0, 0): inf, (0, 1): inf, (1, 0): inf, (1, 1): inf}
            i, aLeft, bLeft = 0, 0, 0

            for j, (aRght, bRght) in enumerate(abPrefs[k:]):

                while i <= j and aRght > aLeft and bRght > bLeft:
                    parity = (aLeft %2, bLeft %2)
                    diff[parity] = min(diff[parity],  aLeft - bLeft)
                    i += 1
                    aLeft, bLeft = abPrefs[i]

                parity = (1 - aRght %2, bRght %2)
                mxDiff = max(mxDiff, aRght - bRght - diff[parity])

        return mxDiff