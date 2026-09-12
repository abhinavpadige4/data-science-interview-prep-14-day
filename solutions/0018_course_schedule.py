"""
LeetCode 207: Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Approach: Topological sorting using Kahn's algorithm (BFS) or DFS to detect cycles.
If there's a cycle in the dependency graph, it's impossible to finish all courses.

Time Complexity: O(V + E) - where V is number of courses, E is number of prerequisites
Space Complexity: O(V + E) - for storing the graph and in-degree/visited arrays
"""

from collections import deque, defaultdict

def can_finish(numCourses, prerequisites):
    """
    Determine if it's possible to finish all courses given prerequisites.
    
    Args:
        numCourses: Total number of courses
        prerequisites: List of prerequisite pairs [course, prerequisite]
        
    Returns:
        True if all courses can be finished, False otherwise
    """
    # Build adjacency list and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    # Construct the graph
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Initialize queue with courses having no prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    courses_taken = 0
    
    # Process courses in topological order
    while queue:
        course = queue.popleft()
        courses_taken += 1
        
        # Reduce in-degree for all dependent courses
        for dependent in graph[course]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    # If we were able to take all courses, return True
    return courses_taken == numCourses

# Alternative DFS approach with cycle detection
def can_finish_dfs(numCourses, prerequisites):
    """
    Determine if it's possible to finish all courses using DFS cycle detection.
    
    Args:
        numCourses: Total number of courses
        prerequisites: List of prerequisite pairs [course, prerequisite]
        
    Returns:
        True if all courses can be finished, False otherwise
    """
    # Build adjacency list
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # 0 = unvisited, 1 = visiting (in current path), 2 = visited
    visited = [0] * numCourses
    
    def has_cycle(course):
        """
        DFS helper to detect cycles.
        """
        if visited[course] == 1:  # Currently in path - cycle detected
            return True
        if visited[course] == 2:  # Already processed
            return False
        
        # Mark as visiting
        visited[course] = 1
        
        # Check all neighbors
        for neighbor in graph[course]:
            if has_cycle(neighbor):
                return True
        
        # Mark as visited
        visited[course] = 2
        return False
    
    # Check for cycles in all courses
    for course in range(numCourses):
        if visited[course] == 0:  # Unvisited
            if has_cycle(course):
                return False
    
    return True

# Test cases
if __name__ == "__main__":
    # Test case 1
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print(f"Input: numCourses = {numCourses1}, prerequisites = {prerequisites1}")
    print(f"Output: {can_finish(numCourses1, prerequisites1)}")  # Expected: True
    print()
    
    # Test case 2
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print(f"Input: numCourses = {numCourses2}, prerequisites = {prerequisites2}")
    print(f"Output: {can_finish(numCourses2, prerequisites2)}")  # Expected: False
    print()
    
    # Test case 3
    numCourses3 = 3
    prerequisites3 = [[1, 0], [2, 1], [3, 2]]
    print(f"Input: numCourses = {numCourses3}, prerequisites = {prerequisites3}")
    print(f"Output: {can_finish(numCourses3, prerequisites3)}")  # Expected: True