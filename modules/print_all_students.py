class Print_All_Students:
    def __init__(self, student):
        self.student_data = student

    def print_all_students(self):
        print("\n======= All Student Information =======")
        for student in self.student_data.allstudents:
            return (student)
        print("\n=========== Nothing Follows ===========\n")