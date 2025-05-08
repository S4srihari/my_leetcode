class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        l = [i for i in dic.items()]
        l.sort(key = lambda x: x[1], reverse = True)
        topK = []
        for i in range(k):
            topK.append(l[i][0])
        return topK"""

        c = Counter(nums)
        top = c.most_common()
        topk = [k for k,v in top[:k]]
        return topk