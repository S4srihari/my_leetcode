"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Breadth first search
        """total = 0
        q = []
        q.append(id)
        while q:
            id = q.pop(0)
            for i in employees:
                if i.id == id:
                    total += i.importance
                    for j in i.subordinates:
                        q.append(j)
        return total"""       

        # Depth first search
        d = {emp.id : emp for emp in employees}
        def dfs(emp):
            imp = emp.importance
            for e in emp.subordinates:
                imp += dfs(d[e]) 
            return imp    
        return dfs(d[id])