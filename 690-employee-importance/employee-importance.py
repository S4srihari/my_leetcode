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
        total = 0
        visited = set()
        q = []
        q.append(id)
        while q:
            id = q.pop(0)
            for i in employees:
                if i.id == id:
                    total += i.importance
                    for j in i.subordinates:
                        q.append(j)
        return total            