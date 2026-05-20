class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        check_count = 0

        while students and check_count < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                check_count = 0
            else:
                students.append(students.pop(0))
                check_count += 1

        return len(students)