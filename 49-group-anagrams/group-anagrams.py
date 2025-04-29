class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for string in strs :
            """c = [0]*26
            for char in string:
                c[ord(char)-ord('a')] += 1
            dic[tuple(c)].append(string)"""
            sort_str = "".join(sorted(string))
            dic[sort_str].append(string)
        return  list(dic.values())