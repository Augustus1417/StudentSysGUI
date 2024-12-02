class Login:
    def __init__(self, student):
        self.student_data = student

    def login(self, id_number):
        if id_number == "": return "You did not type an ID.", False
        for student in self.student_data.allstudents:
            if student.idnum == id_number: 
                return f"Welcome, {student.name}!", True
        return f"The Student with the ID number {id_number} does not exist", False