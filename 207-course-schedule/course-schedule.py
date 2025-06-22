class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """adj_lis = defaultdict(list)
        for pre in prerequisites :
            adj_lis[pre[0]].append(pre[1])
        course_com = [False]*numCourses
        
        def dfs(course,lis):
            if not adj_lis[course]:
                course_com[course] = True
                return True
            elif course_com[course]:
                return True
            temp = []
            for req in adj_lis[course]:
                if req in lis:
                    return False
                else:
                    lis.append(course)
                    temp.append(dfs(req,lis))
                    lis.pop()
            if all(temp):
                course_com[course] = True
                return True

        for i in range(numCourses):
            if not adj_lis[i]:
                course_com[i] = True
            if not course_com[i]:
                dfs(i,[])
            if course_com[i] == False:
                return False
        return True"""

        adj_lis = defaultdict(list)
        for c,p in prerequisites :
            adj_lis[c].append(p)

        visited = set()
        path = set()
        
        def dfs(course, path):
            if course in visited:
                return True
            elif course in path:
                return False
            else :
                path.add(course)
                for req in adj_lis[course]:
                    if not dfs(req,path):
                        return False
                path.remove(course)
                visited.add(course)
                return True
        
        for course in range(numCourses):
            if course not in visited and not dfs(course,path):
                return False
        return True