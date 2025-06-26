class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pos_partitions = []

        def find(st, lis):
            if not st:
                pos_partitions.append(lis[:])
            else :
                for idx in range(len(st)):
                    if st[:idx+1] == st[:idx+1][::-1]:
                        lis.append(st[:idx+1])
                        find(st[idx+1:],lis)
                        lis.pop()
            return
        
        find(s,[])
        return pos_partitions