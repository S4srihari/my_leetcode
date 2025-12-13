class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid = []
        validBL = ["electronics", "grocery", "pharmacy", "restaurant"]

        def check(st):
            if not st:
                return False
            for ch in st:
                if not ch.isalnum() and ch != "_":
                    return False
            return True
        for idx in range(len(code)):
            if not check(code[idx]) or businessLine[idx] not in validBL or not isActive[idx]:
                continue
            valid.append(idx)
        valid.sort(key = lambda x: (businessLine[x], code[x]))
        return [code[i] for i in valid]