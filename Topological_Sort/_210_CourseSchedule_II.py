from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        return self.bfs(graph, indegree, numCourses)

    def bfs(self, graph, indegree, numCourses):
        queue = deque()
        result = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                result.append(i)

        count = 0
        while queue:
            course = queue.popleft()
            count += 1

            for neighbor in graph.get(course, []):
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    result.append(neighbor)

        return result if count == numCourses else []  # Check for cycle