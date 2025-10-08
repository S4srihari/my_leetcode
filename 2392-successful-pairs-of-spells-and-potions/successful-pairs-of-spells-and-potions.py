class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = []
        for i in spells:
            ans.append(m-bisect_left(potions,success/i))
        return ans