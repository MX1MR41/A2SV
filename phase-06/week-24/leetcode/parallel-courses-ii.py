class Solution:
    def minNumberOfSemesters(self, num_courses: int, prerequisites: List[List[int]], max_courses_per_semester: int) -> int:
        # bit manipulation + topological sort + queue
        # Initialize the bitwise representation for the prerequisites of each course
        prereq_masks = [0] * (num_courses + 1)
      
        # Populate the prerequisite mask for each course
        for x, y in prerequisites:
            prereq_masks[y] |= 1 << x
      
        # Initialize the queue with the starting point (0 courses taken, 0 semesters passed)
        queue = deque([(0, 0)])
        visited = {0}  # Set to hold visited states to avoid revisiting
      
        while queue:
            courses_taken, semesters = queue.popleft()
          
            # If all courses have been taken, return the number of semesters it took
            if courses_taken == (1 << (num_courses + 1)) - 2:
                return semesters
          
            # Find the courses that are now free to be taken
            eligible_courses = 0
            for i in range(1, num_courses + 1):
                if (courses_taken & prereq_masks[i]) == prereq_masks[i]:
                    eligible_courses |= 1 << i

            eligible_courses ^= courses_taken # remove the courses that were taken before
          
            # If the number of eligible courses is less than or equal to the max per semester, take them all
            if bin(eligible_courses).count('1') <= max_courses_per_semester:
                next_state = eligible_courses | courses_taken
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, semesters + 1))
            else:
                # If we have more courses available than we can take, choose max allowed number of courses
                course_combinations = eligible_courses
                while eligible_courses:
                    # If the combination is valid, consider it as a possibility and add to the queue
                    if bin(eligible_courses).count('1') == max_courses_per_semester and ((eligible_courses | courses_taken) not in visited):
                        visited.add(eligible_courses | courses_taken)
                        queue.append((eligible_courses | courses_taken, semesters + 1))
                    # Use bitmask to find the next combination of courses
                    # by continually subtracting 1 to get the next possible subset plus
                    # AND-ING with course_combinations to ensure no foreign course is included
                    eligible_courses = (eligible_courses - 1) & course_combinations
