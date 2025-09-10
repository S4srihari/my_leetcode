class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cantCom = set()
        for u,v in friendships:
            canCom = False
            langSet = set(languages[v-1])
            for lang in languages[u-1]:
                if lang in langSet:
                    canCom = True
                    break
            if not canCom:
                cantCom.add(u-1)
                cantCom.add(v-1)

        hashMap = [0]*n
        popLan = 0
        for per in cantCom:
            for lang in languages[per]:
                hashMap[lang-1] += 1
                popLan = max(popLan, hashMap[lang-1])
        return len(cantCom)-popLan