from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        graph = defaultdict(list)
        self.buildGraph(graph, prerequisites, indegrees)
        return self.bfs(graph, numCourses, indegrees)

    # Build the graph and calculate indegree for each course
    def buildGraph(self, graph: defaultdict, prerequisites: List[List[int]], indegrees: List[int]) -> None:
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])  # Add course that depends on the current prerequisite
            indegrees[prereq[0]] += 1

    def bfs(self, graph: defaultdict, numCourses: int, indegree: List[int]) -> bool:
        queue = deque()
        # Enqueue courses with no prerequisites
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0  # Count the number of courses we can take
        while queue:
            course = queue.popleft()
            count += 1
            # Check if current course is a prerequisite for other courses
            for in_course in graph[course]:
                indegree[in_course] -= 1
                if indegree[in_course] == 0:
                    queue.append(in_course)

        return count == numCourses
