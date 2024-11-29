class SearchStudent:
    def __init__(self, student):
        self.student_data = student

    def search_student(self, id_number):
        for student in self.student_data.allstudents:
            if id_number == "": return("\nYou did not type an ID.\n")
            if student.idnum == id_number:
                return(student)
        return(f"\nThe Student with the ID number {id_number} does not exist\n")