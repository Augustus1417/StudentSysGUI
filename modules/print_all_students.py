class Print_All_Students:
    def __init__(self, student):
        self.student_data = student

    def print_all_students(self):
        students = [str(student) for student in self.student_data.allstudents]
        return '\n\n'.join(students)