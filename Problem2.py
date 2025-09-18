# Problem 2
# Course Schedule (https://leetcode.com/problems/course-schedule/)

# V - num of vertices
# E - num of edges
# Time Complexity : O(V + E)
# Space Complexity : O(V + E) -- creating the adjacency list based on hash map
# Did this code successfully run on GFG : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# create graph in form of adjacency list from edge list
# create adjacency list in form of map because we want improve searching
# the courses that are dependent on current independent courses
# we create mapping of independent : dependent
# we keep track of indegrees of all courses
# we traverse through graph using BFS starting from all independent courses ie indegree = 0
# as we keep completing courses we keep reducing indegree of the correspoding 
# dependent courses. We only add courses to the queue once its indegree becomes zero

from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # create graph in form of adjacency list from edge list
        # create adjacency list in form of map because we want improve searching
        # the courses that are dependent on current independent courses
        # we create mapping of independent : dependent
        # we keep track of indegrees of all courses
        # we traverse through graph using BFS starting from all independent courses ie indegree = 0
        # as we keep completing courses we keep reducing indegree of the correspoding 
        # dependent courses. We only add courses to the queue once its indegree becomes zero

        indegree = [0] * numCourses
        courseGraph = {}

        for i in range(len(prerequisites)):
            independent = prerequisites[i][1]
            dependent = prerequisites[i][0]
            # indegree
            indegree[dependent] += 1
            
            # creating graph
            if(independent not in courseGraph):
                courseGraph[independent] = []

            courseGraph[independent].append(dependent)

        que = deque()
        # to keep track of completed courses
        count = 0
        
        # since we are doing BFS so all the children at the same level should be processed together
        # so all courses with indegree = 0 would go in the queue
        for i in range(len(indegree)):
            if(indegree[i] == 0):
                count += 1
                que.append(i)

        if(count == 0):
            # all our courses are dependent on each other
            # there is no course with indegree = 0
            return False

        if(count == numCourses):
            # all courses are independent
            return True

        # BFS
        while(que):
            currCourse = que.popleft()
            if(currCourse in courseGraph):
                for child in courseGraph[currCourse]:
                    # reduce the indegree
                    indegree[child] -= 1
                    if(indegree[child] == 0):
                        # it is independent now. we can take the course now.
                        count += 1
                        que.append(child)

                    if(count == numCourses):
                        # all courses are independent
                        return True

        return False


sol = Solution()
print(sol.canFinish(2, [[1,0]]))
print(sol.canFinish(2, [[1,0],[0,1]]))
print(sol.canFinish(7, [[1, 0], [4, 1], [5, 4], [3, 2], [2, 0], [5, 2], [5, 3], [3, 1], [6, 1]]))
print(sol.canFinish(5, [[1,0], [2,1], [3,2], [4,3], [2,4]]))