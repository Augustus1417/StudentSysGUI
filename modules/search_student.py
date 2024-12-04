class SearchStudent:
    def __init__(self, student):
        self.student_data = student

    def search_student(self, id_number):
        for student in self.student_data.allstudents:
            if id_number == "": return("You did not type an ID.")
            if student.idnum == id_number:
                return(student)
        return(f"The Student with the ID number {id_number} does not exist")