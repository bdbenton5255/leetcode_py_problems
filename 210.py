class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        order = []
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)
        
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        def dfs(i):
            if states[i] == VISITING:
                return False
            elif states[i] == VISITED:
                return True
            states[i] = VISITING

            for nei in g[i]:
                if not dfs(nei):
                    return False
            states[i] = VISITED
            order.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order