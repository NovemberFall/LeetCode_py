from collections import deque, defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        graph = defaultdict(list)
        self.buildGraph(graph, prerequisites, indegrees)
        return self.bfs(graph, numCourses, indegrees)

    def buildGraph(self, graph: defaultdict, prerequisites: List[List[int]], indegrees: List[int]) -> None:
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            indegrees[prereq[0]] += 1

    def bfs(self, graph: defaultdict, numCourses: int, indegrees: List[int]) -> List[int]:
        res = []
        queue = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            cur_course = queue.popleft()
            count += 1
            res.append(cur_course)
            for in_course in graph[cur_course]:
                indegrees[in_course] -= 1
                if indegrees[in_course] == 0:
                    queue.append(in_course)

        return res if count == numCourses else []
